import json

import pytest

delete_example = (
    {"myKey": "myValue"},
    {"btType": "BTJEditDelete-1992",
     "path": {"btType": "BTJPath-3073", "startNode": "", "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]}},
    {}
)
insert_example = (
    {},
    {"btType": "BTJEditInsert-2523",
     "path": {"btType": "BTJPath-3073", "startNode": "", "path": [{"btType": "BTJPathKey-3221", "key": "insertedKey"}]},
     "value": "myValue"},
    {"insertedKey": "myValue"}
)
change_example = (
    {"myKey": "myValue"},
    {"btType": "BTJEditChange-2636",
     "path": {"btType": "BTJPath-3073", "startNode": "", "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]},
     "value": "myOtherValue"},
    {"myKey": "myOtherValue"}
)
move_example = (
    {"myKey": "myValue"},
    {"btType": "BTJEditMove-3245", "sourcePath": {"btType": "BTJPath-3073", "startNode": "",
                                                  "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]},
     "destinationPath": {"btType": "BTJPath-3073", "startNode": "",
                         "path": [{"btType": "BTJPathKey-3221", "key": "keyCreatedFromMove"}]}},
    {"keyCreatedFromMove": "myValue"}
)
list_example = (
    {},
    {"btType": "BTJEditList-2707", "edits": [
        {"btType": "BTJEditInsert-2523", "path": {"btType": "BTJPath-3073", "startNode": "", "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]},
         "value": "myValue"},
        {"btType": "BTJEditChange-2636", "path": {"btType": "BTJPath-3073", "startNode": "",
                                                  "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]},
         "value": ["firstValue", "secondValue"]},
        {"btType": "BTJEditInsert-2523", "path": {"btType": "BTJPath-3073", "startNode": "",
                                                  "path": [{"btType": "BTJPathKey-3221", "key": "myKey"},
                                                           {"btType": "BTJPathIndex-1871", "index": 1}]},
         "value": "myBetterSecondValue"},
        {"btType": "BTJEditDelete-1992", "path": {"btType": "BTJPath-3073", "startNode": "",
                                                  "path": [{"btType": "BTJPathKey-3221", "key": "myKey"},
                                                           {"btType": "BTJPathIndex-1871", "index": 2}]}}
    ]},
    {"myKey": ["firstValue", "myBetterSecondValue"]}
)


@pytest.mark.parametrize("start_json, edit_json, expected_json",
                         [delete_example, insert_example, change_example, move_example, list_example],
                         ids=["delete_example", "insert_example", "change_example", "move_example", "list_example"])
def test_documentation_examples(start_json, edit_json, expected_json, new_document, client):
    new_element = create_app_element(client, new_document.did, new_document.default_workspace, start_json)
    update_app_element(client, new_document.did, new_document.default_workspace, new_element["elementId"], edit_json)
    assert get_json_tree(client, new_document.did, new_document.default_workspace,
                         new_element["elementId"]) == expected_json


def create_app_element(client, did, wid, json_tree):
    """Currently not supported by the client, but will be soon. In the meantime, this creates the request."""
    result = client.api_client.request(
        method="POST",
        url=f"{client.configuration.host}/api/appelements/d/{did}/w/{wid}",
        headers={
            "Accept": "application/vnd.onshape.v1+json;charset=utf-8;qs=0.1, application/json;charset=utf-8; qs=0.09"
        },
        body={"name": "Test", "jsonTree": json_tree, "formatId": "test/test"},
    )
    return json.loads(result.data)


def update_app_element(client, did, wid, eid, json_tree_edit):
    """Currently not supported by the client, but will be soon. In the meantime, this creates the request."""
    result = client.api_client.request(
        method="POST",
        url=f"{client.configuration.host}/api/appelements/d/{did}/w/{wid}/e/{eid}/content",
        headers={
            "Accept": "application/vnd.onshape.v1+json;charset=utf-8;qs=0.1, application/json;charset=utf-8; qs=0.09"
        },
        body={"jsonTreeEdit": json_tree_edit},
    )
    return json.loads(result.data)


def get_json_tree(client, did, wid, eid):
    """Currently not supported by the client, but will be soon. In the meantime, this creates the request."""
    result = client.api_client.request(
        method="GET",
        url=f"{client.configuration.host}/api/appelements/d/{did}/w/{wid}/e/{eid}/content/json",
        headers={
            "Accept": "application/vnd.onshape.v2+json;charset=utf-8;qs=0.1"
        }
    )
    # strip the _nodeId values
    return {k: v for k, v in json.loads(result.data)["tree"].items() if not k == "_nodeId"}

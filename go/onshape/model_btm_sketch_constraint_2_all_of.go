/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.122
 * Contact: api-support@onshape.zendesk.com
 */

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package onshape

import (
	"encoding/json"
)

// BTMSketchConstraint2AllOf struct for BTMSketchConstraint2AllOf
type BTMSketchConstraint2AllOf struct {
	BtType              *string    `json:"btType,omitempty"`
	ConstraintType      *string    `json:"constraintType,omitempty"`
	DrivenDimension     *bool      `json:"drivenDimension,omitempty"`
	HasOffsetData1      *bool      `json:"hasOffsetData1,omitempty"`
	HasOffsetData2      *bool      `json:"hasOffsetData2,omitempty"`
	HasPierceParameter_ *bool      `json:"hasPierceParameter,omitempty"`
	HelpParameters      *[]float64 `json:"helpParameters,omitempty"`
	OffsetDistance1     *float64   `json:"offsetDistance1,omitempty"`
	OffsetDistance2     *float64   `json:"offsetDistance2,omitempty"`
	OffsetOrientation1  *bool      `json:"offsetOrientation1,omitempty"`
	OffsetOrientation2  *bool      `json:"offsetOrientation2,omitempty"`
	PierceParameter     *float64   `json:"pierceParameter,omitempty"`
}

// NewBTMSketchConstraint2AllOf instantiates a new BTMSketchConstraint2AllOf object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewBTMSketchConstraint2AllOf() *BTMSketchConstraint2AllOf {
	this := BTMSketchConstraint2AllOf{}
	return &this
}

// NewBTMSketchConstraint2AllOfWithDefaults instantiates a new BTMSketchConstraint2AllOf object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewBTMSketchConstraint2AllOfWithDefaults() *BTMSketchConstraint2AllOf {
	this := BTMSketchConstraint2AllOf{}
	return &this
}

// GetBtType returns the BtType field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetBtType() string {
	if o == nil || o.BtType == nil {
		var ret string
		return ret
	}
	return *o.BtType
}

// GetBtTypeOk returns a tuple with the BtType field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetBtTypeOk() (*string, bool) {
	if o == nil || o.BtType == nil {
		return nil, false
	}
	return o.BtType, true
}

// HasBtType returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasBtType() bool {
	if o != nil && o.BtType != nil {
		return true
	}

	return false
}

// SetBtType gets a reference to the given string and assigns it to the BtType field.
func (o *BTMSketchConstraint2AllOf) SetBtType(v string) {
	o.BtType = &v
}

// GetConstraintType returns the ConstraintType field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetConstraintType() string {
	if o == nil || o.ConstraintType == nil {
		var ret string
		return ret
	}
	return *o.ConstraintType
}

// GetConstraintTypeOk returns a tuple with the ConstraintType field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetConstraintTypeOk() (*string, bool) {
	if o == nil || o.ConstraintType == nil {
		return nil, false
	}
	return o.ConstraintType, true
}

// HasConstraintType returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasConstraintType() bool {
	if o != nil && o.ConstraintType != nil {
		return true
	}

	return false
}

// SetConstraintType gets a reference to the given string and assigns it to the ConstraintType field.
func (o *BTMSketchConstraint2AllOf) SetConstraintType(v string) {
	o.ConstraintType = &v
}

// GetDrivenDimension returns the DrivenDimension field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetDrivenDimension() bool {
	if o == nil || o.DrivenDimension == nil {
		var ret bool
		return ret
	}
	return *o.DrivenDimension
}

// GetDrivenDimensionOk returns a tuple with the DrivenDimension field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetDrivenDimensionOk() (*bool, bool) {
	if o == nil || o.DrivenDimension == nil {
		return nil, false
	}
	return o.DrivenDimension, true
}

// HasDrivenDimension returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasDrivenDimension() bool {
	if o != nil && o.DrivenDimension != nil {
		return true
	}

	return false
}

// SetDrivenDimension gets a reference to the given bool and assigns it to the DrivenDimension field.
func (o *BTMSketchConstraint2AllOf) SetDrivenDimension(v bool) {
	o.DrivenDimension = &v
}

// GetHasOffsetData1 returns the HasOffsetData1 field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetHasOffsetData1() bool {
	if o == nil || o.HasOffsetData1 == nil {
		var ret bool
		return ret
	}
	return *o.HasOffsetData1
}

// GetHasOffsetData1Ok returns a tuple with the HasOffsetData1 field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetHasOffsetData1Ok() (*bool, bool) {
	if o == nil || o.HasOffsetData1 == nil {
		return nil, false
	}
	return o.HasOffsetData1, true
}

// HasHasOffsetData1 returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasHasOffsetData1() bool {
	if o != nil && o.HasOffsetData1 != nil {
		return true
	}

	return false
}

// SetHasOffsetData1 gets a reference to the given bool and assigns it to the HasOffsetData1 field.
func (o *BTMSketchConstraint2AllOf) SetHasOffsetData1(v bool) {
	o.HasOffsetData1 = &v
}

// GetHasOffsetData2 returns the HasOffsetData2 field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetHasOffsetData2() bool {
	if o == nil || o.HasOffsetData2 == nil {
		var ret bool
		return ret
	}
	return *o.HasOffsetData2
}

// GetHasOffsetData2Ok returns a tuple with the HasOffsetData2 field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetHasOffsetData2Ok() (*bool, bool) {
	if o == nil || o.HasOffsetData2 == nil {
		return nil, false
	}
	return o.HasOffsetData2, true
}

// HasHasOffsetData2 returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasHasOffsetData2() bool {
	if o != nil && o.HasOffsetData2 != nil {
		return true
	}

	return false
}

// SetHasOffsetData2 gets a reference to the given bool and assigns it to the HasOffsetData2 field.
func (o *BTMSketchConstraint2AllOf) SetHasOffsetData2(v bool) {
	o.HasOffsetData2 = &v
}

// GetHasPierceParameter returns the HasPierceParameter field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetHasPierceParameter() bool {
	if o == nil || o.HasPierceParameter_ == nil {
		var ret bool
		return ret
	}
	return *o.HasPierceParameter_
}

// GetHasPierceParameterOk returns a tuple with the HasPierceParameter field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetHasPierceParameterOk() (*bool, bool) {
	if o == nil || o.HasPierceParameter_ == nil {
		return nil, false
	}
	return o.HasPierceParameter_, true
}

// HasHasPierceParameter returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasHasPierceParameter() bool {
	if o != nil && o.HasPierceParameter_ != nil {
		return true
	}

	return false
}

// SetHasPierceParameter gets a reference to the given bool and assigns it to the HasPierceParameter field.
func (o *BTMSketchConstraint2AllOf) SetHasPierceParameter(v bool) {
	o.HasPierceParameter_ = &v
}

// GetHelpParameters returns the HelpParameters field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetHelpParameters() []float64 {
	if o == nil || o.HelpParameters == nil {
		var ret []float64
		return ret
	}
	return *o.HelpParameters
}

// GetHelpParametersOk returns a tuple with the HelpParameters field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetHelpParametersOk() (*[]float64, bool) {
	if o == nil || o.HelpParameters == nil {
		return nil, false
	}
	return o.HelpParameters, true
}

// HasHelpParameters returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasHelpParameters() bool {
	if o != nil && o.HelpParameters != nil {
		return true
	}

	return false
}

// SetHelpParameters gets a reference to the given []float64 and assigns it to the HelpParameters field.
func (o *BTMSketchConstraint2AllOf) SetHelpParameters(v []float64) {
	o.HelpParameters = &v
}

// GetOffsetDistance1 returns the OffsetDistance1 field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetOffsetDistance1() float64 {
	if o == nil || o.OffsetDistance1 == nil {
		var ret float64
		return ret
	}
	return *o.OffsetDistance1
}

// GetOffsetDistance1Ok returns a tuple with the OffsetDistance1 field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetOffsetDistance1Ok() (*float64, bool) {
	if o == nil || o.OffsetDistance1 == nil {
		return nil, false
	}
	return o.OffsetDistance1, true
}

// HasOffsetDistance1 returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasOffsetDistance1() bool {
	if o != nil && o.OffsetDistance1 != nil {
		return true
	}

	return false
}

// SetOffsetDistance1 gets a reference to the given float64 and assigns it to the OffsetDistance1 field.
func (o *BTMSketchConstraint2AllOf) SetOffsetDistance1(v float64) {
	o.OffsetDistance1 = &v
}

// GetOffsetDistance2 returns the OffsetDistance2 field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetOffsetDistance2() float64 {
	if o == nil || o.OffsetDistance2 == nil {
		var ret float64
		return ret
	}
	return *o.OffsetDistance2
}

// GetOffsetDistance2Ok returns a tuple with the OffsetDistance2 field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetOffsetDistance2Ok() (*float64, bool) {
	if o == nil || o.OffsetDistance2 == nil {
		return nil, false
	}
	return o.OffsetDistance2, true
}

// HasOffsetDistance2 returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasOffsetDistance2() bool {
	if o != nil && o.OffsetDistance2 != nil {
		return true
	}

	return false
}

// SetOffsetDistance2 gets a reference to the given float64 and assigns it to the OffsetDistance2 field.
func (o *BTMSketchConstraint2AllOf) SetOffsetDistance2(v float64) {
	o.OffsetDistance2 = &v
}

// GetOffsetOrientation1 returns the OffsetOrientation1 field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetOffsetOrientation1() bool {
	if o == nil || o.OffsetOrientation1 == nil {
		var ret bool
		return ret
	}
	return *o.OffsetOrientation1
}

// GetOffsetOrientation1Ok returns a tuple with the OffsetOrientation1 field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetOffsetOrientation1Ok() (*bool, bool) {
	if o == nil || o.OffsetOrientation1 == nil {
		return nil, false
	}
	return o.OffsetOrientation1, true
}

// HasOffsetOrientation1 returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasOffsetOrientation1() bool {
	if o != nil && o.OffsetOrientation1 != nil {
		return true
	}

	return false
}

// SetOffsetOrientation1 gets a reference to the given bool and assigns it to the OffsetOrientation1 field.
func (o *BTMSketchConstraint2AllOf) SetOffsetOrientation1(v bool) {
	o.OffsetOrientation1 = &v
}

// GetOffsetOrientation2 returns the OffsetOrientation2 field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetOffsetOrientation2() bool {
	if o == nil || o.OffsetOrientation2 == nil {
		var ret bool
		return ret
	}
	return *o.OffsetOrientation2
}

// GetOffsetOrientation2Ok returns a tuple with the OffsetOrientation2 field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetOffsetOrientation2Ok() (*bool, bool) {
	if o == nil || o.OffsetOrientation2 == nil {
		return nil, false
	}
	return o.OffsetOrientation2, true
}

// HasOffsetOrientation2 returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasOffsetOrientation2() bool {
	if o != nil && o.OffsetOrientation2 != nil {
		return true
	}

	return false
}

// SetOffsetOrientation2 gets a reference to the given bool and assigns it to the OffsetOrientation2 field.
func (o *BTMSketchConstraint2AllOf) SetOffsetOrientation2(v bool) {
	o.OffsetOrientation2 = &v
}

// GetPierceParameter returns the PierceParameter field value if set, zero value otherwise.
func (o *BTMSketchConstraint2AllOf) GetPierceParameter() float64 {
	if o == nil || o.PierceParameter == nil {
		var ret float64
		return ret
	}
	return *o.PierceParameter
}

// GetPierceParameterOk returns a tuple with the PierceParameter field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMSketchConstraint2AllOf) GetPierceParameterOk() (*float64, bool) {
	if o == nil || o.PierceParameter == nil {
		return nil, false
	}
	return o.PierceParameter, true
}

// HasPierceParameter returns a boolean if a field has been set.
func (o *BTMSketchConstraint2AllOf) HasPierceParameter() bool {
	if o != nil && o.PierceParameter != nil {
		return true
	}

	return false
}

// SetPierceParameter gets a reference to the given float64 and assigns it to the PierceParameter field.
func (o *BTMSketchConstraint2AllOf) SetPierceParameter(v float64) {
	o.PierceParameter = &v
}

func (o BTMSketchConstraint2AllOf) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.BtType != nil {
		toSerialize["btType"] = o.BtType
	}
	if o.ConstraintType != nil {
		toSerialize["constraintType"] = o.ConstraintType
	}
	if o.DrivenDimension != nil {
		toSerialize["drivenDimension"] = o.DrivenDimension
	}
	if o.HasOffsetData1 != nil {
		toSerialize["hasOffsetData1"] = o.HasOffsetData1
	}
	if o.HasOffsetData2 != nil {
		toSerialize["hasOffsetData2"] = o.HasOffsetData2
	}
	if o.HasPierceParameter_ != nil {
		toSerialize["hasPierceParameter"] = o.HasPierceParameter
	}
	if o.HelpParameters != nil {
		toSerialize["helpParameters"] = o.HelpParameters
	}
	if o.OffsetDistance1 != nil {
		toSerialize["offsetDistance1"] = o.OffsetDistance1
	}
	if o.OffsetDistance2 != nil {
		toSerialize["offsetDistance2"] = o.OffsetDistance2
	}
	if o.OffsetOrientation1 != nil {
		toSerialize["offsetOrientation1"] = o.OffsetOrientation1
	}
	if o.OffsetOrientation2 != nil {
		toSerialize["offsetOrientation2"] = o.OffsetOrientation2
	}
	if o.PierceParameter != nil {
		toSerialize["pierceParameter"] = o.PierceParameter
	}
	return json.Marshal(toSerialize)
}

type NullableBTMSketchConstraint2AllOf struct {
	value *BTMSketchConstraint2AllOf
	isSet bool
}

func (v NullableBTMSketchConstraint2AllOf) Get() *BTMSketchConstraint2AllOf {
	return v.value
}

func (v *NullableBTMSketchConstraint2AllOf) Set(val *BTMSketchConstraint2AllOf) {
	v.value = val
	v.isSet = true
}

func (v NullableBTMSketchConstraint2AllOf) IsSet() bool {
	return v.isSet
}

func (v *NullableBTMSketchConstraint2AllOf) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableBTMSketchConstraint2AllOf(val *BTMSketchConstraint2AllOf) *NullableBTMSketchConstraint2AllOf {
	return &NullableBTMSketchConstraint2AllOf{value: val, isSet: true}
}

func (v NullableBTMSketchConstraint2AllOf) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableBTMSketchConstraint2AllOf) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}

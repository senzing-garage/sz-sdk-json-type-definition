// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public class SzDiagnosticGetFeatureResponse {
    @JsonValue
    private GetFeature value;

    public SzDiagnosticGetFeatureResponse() {
    }

    @JsonCreator
    public SzDiagnosticGetFeatureResponse(GetFeature value) {
        this.value = value;
    }

    public GetFeature getValue() {
        return value;
    }

    public void setValue(GetFeature value) {
        this.value = value;
    }
}

// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public class SzEngineFindPathByEntityIdResponse {
    @JsonValue
    private Path value;

    public SzEngineFindPathByEntityIdResponse() {
    }

    @JsonCreator
    public SzEngineFindPathByEntityIdResponse(Path value) {
        this.value = value;
    }

    public Path getValue() {
        return value;
    }

    public void setValue(Path value) {
        this.value = value;
    }
}
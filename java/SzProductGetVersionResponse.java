// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public class SzProductGetVersionResponse {
    @JsonValue
    private ProductVersion value;

    public SzProductGetVersionResponse() {
    }

    @JsonCreator
    public SzProductGetVersionResponse(ProductVersion value) {
        this.value = value;
    }

    public ProductVersion getValue() {
        return value;
    }

    public void setValue(ProductVersion value) {
        this.value = value;
    }
}

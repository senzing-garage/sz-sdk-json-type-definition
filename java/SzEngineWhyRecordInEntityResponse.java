// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public class SzEngineWhyRecordInEntityResponse {
    @JsonValue
    private WhyRecordInEntity value;

    public SzEngineWhyRecordInEntityResponse() {
    }

    @JsonCreator
    public SzEngineWhyRecordInEntityResponse(WhyRecordInEntity value) {
        this.value = value;
    }

    public WhyRecordInEntity getValue() {
        return value;
    }

    public void setValue(WhyRecordInEntity value) {
        this.value = value;
    }
}

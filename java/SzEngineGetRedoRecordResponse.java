// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public class SzEngineGetRedoRecordResponse {
    @JsonValue
    private RedoRecord value;

    public SzEngineGetRedoRecordResponse() {
    }

    @JsonCreator
    public SzEngineGetRedoRecordResponse(RedoRecord value) {
        this.value = value;
    }

    public RedoRecord getValue() {
        return value;
    }

    public void setValue(RedoRecord value) {
        this.value = value;
    }
}

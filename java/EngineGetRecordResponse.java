// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

/**
 * No description.
 */
public class EngineGetRecordResponse {
    @JsonValue
    private Record value;

    public EngineGetRecordResponse() {
    }

    @JsonCreator
    public EngineGetRecordResponse(Record value) {
        this.value = value;
    }

    public Record getValue() {
        return value;
    }

    public void setValue(Record value) {
        this.value = value;
    }
}
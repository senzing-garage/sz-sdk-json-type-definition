// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

/**
 * No description.
 */
public class EngineSearchByAttributesResponse {
    @JsonValue
    private Search value;

    public EngineSearchByAttributesResponse() {
    }

    @JsonCreator
    public EngineSearchByAttributesResponse(Search value) {
        this.value = value;
    }

    public Search getValue() {
        return value;
    }

    public void setValue(Search value) {
        this.value = value;
    }
}

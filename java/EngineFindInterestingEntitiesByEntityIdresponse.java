// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

/**
 * No description.
 */
public class EngineFindInterestingEntitiesByEntityIdresponse {
    @JsonValue
    private Interesting value;

    public EngineFindInterestingEntitiesByEntityIdresponse() {
    }

    @JsonCreator
    public EngineFindInterestingEntitiesByEntityIdresponse(Interesting value) {
        this.value = value;
    }

    public Interesting getValue() {
        return value;
    }

    public void setValue(Interesting value) {
        this.value = value;
    }
}

// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public class Stats {
    @JsonValue
    private FixmeUnknown value;

    public Stats() {
    }

    @JsonCreator
    public Stats(FixmeUnknown value) {
        this.value = value;
    }

    public FixmeUnknown getValue() {
        return value;
    }

    public void setValue(FixmeUnknown value) {
        this.value = value;
    }
}

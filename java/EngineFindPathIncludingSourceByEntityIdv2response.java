// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

/**
 * No description.
 */
public class EngineFindPathIncludingSourceByEntityIdv2response {
    @JsonValue
    private Path value;

    public EngineFindPathIncludingSourceByEntityIdv2response() {
    }

    @JsonCreator
    public EngineFindPathIncludingSourceByEntityIdv2response(Path value) {
        this.value = value;
    }

    public Path getValue() {
        return value;
    }

    public void setValue(Path value) {
        this.value = value;
    }
}
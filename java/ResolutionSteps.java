// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import java.util.List;

/**
 * No description.
 */
public class ResolutionSteps {
    @JsonValue
    private List<ResolutionStep> value;

    public ResolutionSteps() {
    }

    @JsonCreator
    public ResolutionSteps(List<ResolutionStep> value) {
        this.value = value;
    }

    public List<ResolutionStep> getValue() {
        return value;
    }

    public void setValue(List<ResolutionStep> value) {
        this.value = value;
    }
}

// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import java.util.List;

/**
 * No description.
 */
public class DiagnosticGetEntityResumeResponse {
    @JsonValue
    private List<DiagnosticGetEntityResumeResponse0> value;

    public DiagnosticGetEntityResumeResponse() {
    }

    @JsonCreator
    public DiagnosticGetEntityResumeResponse(List<DiagnosticGetEntityResumeResponse0> value) {
        this.value = value;
    }

    public List<DiagnosticGetEntityResumeResponse0> getValue() {
        return value;
    }

    public void setValue(List<DiagnosticGetEntityResumeResponse0> value) {
        this.value = value;
    }
}
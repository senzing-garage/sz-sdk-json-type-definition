// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public class G2engineFindPathIncludingSourceByRecordIdResponse {
    @JsonValue
    private Path value;

    public G2engineFindPathIncludingSourceByRecordIdResponse() {
    }

    @JsonCreator
    public G2engineFindPathIncludingSourceByRecordIdResponse(Path value) {
        this.value = value;
    }

    public Path getValue() {
        return value;
    }

    public void setValue(Path value) {
        this.value = value;
    }
}
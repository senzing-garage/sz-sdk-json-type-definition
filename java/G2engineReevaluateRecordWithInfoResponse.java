// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public class G2engineReevaluateRecordWithInfoResponse {
    @JsonValue
    private WithInfo value;

    public G2engineReevaluateRecordWithInfoResponse() {
    }

    @JsonCreator
    public G2engineReevaluateRecordWithInfoResponse(WithInfo value) {
        this.value = value;
    }

    public WithInfo getValue() {
        return value;
    }

    public void setValue(WithInfo value) {
        this.value = value;
    }
}
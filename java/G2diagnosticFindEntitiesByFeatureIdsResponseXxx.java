// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import java.util.List;

public class G2diagnosticFindEntitiesByFeatureIdsResponseXxx {
    @JsonValue
    private List<G2diagnosticFindEntitiesByFeatureIdsResponseXxx0> value;

    public G2diagnosticFindEntitiesByFeatureIdsResponseXxx() {
    }

    @JsonCreator
    public G2diagnosticFindEntitiesByFeatureIdsResponseXxx(List<G2diagnosticFindEntitiesByFeatureIdsResponseXxx0> value) {
        this.value = value;
    }

    public List<G2diagnosticFindEntitiesByFeatureIdsResponseXxx0> getValue() {
        return value;
    }

    public void setValue(List<G2diagnosticFindEntitiesByFeatureIdsResponseXxx0> value) {
        this.value = value;
    }
}
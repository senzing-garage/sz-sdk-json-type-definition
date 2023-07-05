// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class WhyEntities {
    @JsonProperty("ENTITIES")
    private Entities entities;

    @JsonProperty("WHY_RESULTS")
    private WhyResults whyResults;

    public WhyEntities() {
    }

    /**
     * Getter for entities.<p>
     * No description.
     */
    public Entities getEntities() {
        return entities;
    }

    /**
     * Setter for entities.<p>
     * No description.
     */
    public void setEntities(Entities entities) {
        this.entities = entities;
    }

    /**
     * Getter for whyResults.<p>
     * No description.
     */
    public WhyResults getWhyResults() {
        return whyResults;
    }

    /**
     * Setter for whyResults.<p>
     * No description.
     */
    public void setWhyResults(WhyResults whyResults) {
        this.whyResults = whyResults;
    }
}

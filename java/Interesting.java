// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class Interesting {
    @JsonProperty("INTERESTING_ENTITIES")
    private InterestingEntities interestingEntities;

    public Interesting() {
    }

    /**
     * Getter for interestingEntities.<p>
     * No description.
     */
    public InterestingEntities getInterestingEntities() {
        return interestingEntities;
    }

    /**
     * Setter for interestingEntities.<p>
     * No description.
     */
    public void setInterestingEntities(InterestingEntities interestingEntities) {
        this.interestingEntities = interestingEntities;
    }
}

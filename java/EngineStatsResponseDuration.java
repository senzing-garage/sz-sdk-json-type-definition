// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class EngineStatsResponseDuration {
    @JsonProperty("PATTERN")
    private String pattern;

    @JsonProperty("TYPE")
    private String type;

    public EngineStatsResponseDuration() {
    }

    /**
     * Getter for pattern.<p>
     * No description.
     */
    public String getPattern() {
        return pattern;
    }

    /**
     * Setter for pattern.<p>
     * No description.
     */
    public void setPattern(String pattern) {
        this.pattern = pattern;
    }

    /**
     * Getter for type.<p>
     * No description.
     */
    public String getType() {
        return type;
    }

    /**
     * Setter for type.<p>
     * No description.
     */
    public void setType(String type) {
        this.type = type;
    }
}

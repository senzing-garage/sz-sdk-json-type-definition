// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class WithInfo {
    @JsonProperty("AFFECTED_ENTITIES")
    private AffectedEntities affectedEntities;

    @JsonProperty("DATA_SOURCE")
    private String dataSource;

    @JsonProperty("INTERESTING_ENTITIES")
    private InterestingEntities interestingEntities;

    @JsonProperty("RECORD_ID")
    private String recordId;

    public WithInfo() {
    }

    /**
     * Getter for affectedEntities.<p>
     * No description.
     */
    public AffectedEntities getAffectedEntities() {
        return affectedEntities;
    }

    /**
     * Setter for affectedEntities.<p>
     * No description.
     */
    public void setAffectedEntities(AffectedEntities affectedEntities) {
        this.affectedEntities = affectedEntities;
    }

    /**
     * Getter for dataSource.<p>
     * No description.
     */
    public String getDataSource() {
        return dataSource;
    }

    /**
     * Setter for dataSource.<p>
     * No description.
     */
    public void setDataSource(String dataSource) {
        this.dataSource = dataSource;
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

    /**
     * Getter for recordId.<p>
     * No description.
     */
    public String getRecordId() {
        return recordId;
    }

    /**
     * Setter for recordId.<p>
     * No description.
     */
    public void setRecordId(String recordId) {
        this.recordId = recordId;
    }
}

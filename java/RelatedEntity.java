// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import java.time.OffsetDateTime;
import java.util.List;

@JsonSerialize
public class RelatedEntity {
    @JsonProperty("ENTITY_ID")
    private Integer entityId;

    @JsonProperty("ENTITY_NAME")
    private String entityName;

    @JsonProperty("ERRULE_CODE")
    private String erruleCode;

    @JsonProperty("IS_AMBIGUOUS")
    private Integer isAmbiguous;

    @JsonProperty("IS_DISCLOSED")
    private Integer isDisclosed;

    @JsonProperty("LAST_SEEN_DT")
    private OffsetDateTime lastSeenDt;

    @JsonProperty("MATCH_KEY")
    private String matchKey;

    @JsonProperty("MATCH_LEVEL")
    private Integer matchLevel;

    @JsonProperty("MATCH_LEVEL_CODE")
    private String matchLevelCode;

    @JsonProperty("RECORDS")
    private Records records;

    @JsonProperty("RECORD_SUMMARY")
    private List<RecordSummaryElement> recordSummary;

    public RelatedEntity() {
    }

    /**
     * Getter for entityId.<p>
     * The ENTITY_ID is the Senzing-generated identifier for the discovered
     * entity. It may change when new information is added.
     */
    public Integer getEntityId() {
        return entityId;
    }

    /**
     * Setter for entityId.<p>
     * The ENTITY_ID is the Senzing-generated identifier for the discovered
     * entity. It may change when new information is added.
     */
    public void setEntityId(Integer entityId) {
        this.entityId = entityId;
    }

    /**
     * Getter for entityName.<p>
     */
    public String getEntityName() {
        return entityName;
    }

    /**
     * Setter for entityName.<p>
     */
    public void setEntityName(String entityName) {
        this.entityName = entityName;
    }

    /**
     * Getter for erruleCode.<p>
     */
    public String getErruleCode() {
        return erruleCode;
    }

    /**
     * Setter for erruleCode.<p>
     */
    public void setErruleCode(String erruleCode) {
        this.erruleCode = erruleCode;
    }

    /**
     * Getter for isAmbiguous.<p>
     */
    public Integer getIsAmbiguous() {
        return isAmbiguous;
    }

    /**
     * Setter for isAmbiguous.<p>
     */
    public void setIsAmbiguous(Integer isAmbiguous) {
        this.isAmbiguous = isAmbiguous;
    }

    /**
     * Getter for isDisclosed.<p>
     */
    public Integer getIsDisclosed() {
        return isDisclosed;
    }

    /**
     * Setter for isDisclosed.<p>
     */
    public void setIsDisclosed(Integer isDisclosed) {
        this.isDisclosed = isDisclosed;
    }

    /**
     * Getter for lastSeenDt.<p>
     */
    public OffsetDateTime getLastSeenDt() {
        return lastSeenDt;
    }

    /**
     * Setter for lastSeenDt.<p>
     */
    public void setLastSeenDt(OffsetDateTime lastSeenDt) {
        this.lastSeenDt = lastSeenDt;
    }

    /**
     * Getter for matchKey.<p>
     */
    public String getMatchKey() {
        return matchKey;
    }

    /**
     * Setter for matchKey.<p>
     */
    public void setMatchKey(String matchKey) {
        this.matchKey = matchKey;
    }

    /**
     * Getter for matchLevel.<p>
     */
    public Integer getMatchLevel() {
        return matchLevel;
    }

    /**
     * Setter for matchLevel.<p>
     */
    public void setMatchLevel(Integer matchLevel) {
        this.matchLevel = matchLevel;
    }

    /**
     * Getter for matchLevelCode.<p>
     */
    public String getMatchLevelCode() {
        return matchLevelCode;
    }

    /**
     * Setter for matchLevelCode.<p>
     */
    public void setMatchLevelCode(String matchLevelCode) {
        this.matchLevelCode = matchLevelCode;
    }

    /**
     * Getter for records.<p>
     */
    public Records getRecords() {
        return records;
    }

    /**
     * Setter for records.<p>
     */
    public void setRecords(Records records) {
        this.records = records;
    }

    /**
     * Getter for recordSummary.<p>
     */
    public List<RecordSummaryElement> getRecordSummary() {
        return recordSummary;
    }

    /**
     * Setter for recordSummary.<p>
     */
    public void setRecordSummary(List<RecordSummaryElement> recordSummary) {
        this.recordSummary = recordSummary;
    }
}

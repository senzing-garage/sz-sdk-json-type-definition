// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

@JsonSerialize
public class ProcessResultResolvedEntities {
    @JsonProperty("ENTITY_ID")
    private Integer entityId;

    @JsonProperty("ENTITY_NAME")
    private String entityName;

    @JsonProperty("ERRULE_CODE")
    private String erruleCode;

    @JsonProperty("FEATURES")
    private Features features;

    @JsonProperty("LAST_SEEN_DT")
    private String lastSeenDt;

    @JsonProperty("MATCH_KEY")
    private String matchKey;

    @JsonProperty("MATCH_LEVEL")
    private Integer matchLevel;

    @JsonProperty("MATCH_LEVEL_CODE")
    private String matchLevelCode;

    @JsonProperty("MATCH_SCORES")
    private MatchScores matchScores;

    @JsonProperty("RECORDS")
    private Records records;

    @JsonProperty("RECORD_SUMMARY")
    private RecordSummary recordSummary;

    public ProcessResultResolvedEntities() {
    }

    /**
     * Getter for entityId.<p>
     * No description.
     */
    public Integer getEntityId() {
        return entityId;
    }

    /**
     * Setter for entityId.<p>
     * No description.
     */
    public void setEntityId(Integer entityId) {
        this.entityId = entityId;
    }

    /**
     * Getter for entityName.<p>
     * No description.
     */
    public String getEntityName() {
        return entityName;
    }

    /**
     * Setter for entityName.<p>
     * No description.
     */
    public void setEntityName(String entityName) {
        this.entityName = entityName;
    }

    /**
     * Getter for erruleCode.<p>
     * No description.
     */
    public String getErruleCode() {
        return erruleCode;
    }

    /**
     * Setter for erruleCode.<p>
     * No description.
     */
    public void setErruleCode(String erruleCode) {
        this.erruleCode = erruleCode;
    }

    /**
     * Getter for features.<p>
     * No description.
     */
    public Features getFeatures() {
        return features;
    }

    /**
     * Setter for features.<p>
     * No description.
     */
    public void setFeatures(Features features) {
        this.features = features;
    }

    /**
     * Getter for lastSeenDt.<p>
     * No description.
     */
    public String getLastSeenDt() {
        return lastSeenDt;
    }

    /**
     * Setter for lastSeenDt.<p>
     * No description.
     */
    public void setLastSeenDt(String lastSeenDt) {
        this.lastSeenDt = lastSeenDt;
    }

    /**
     * Getter for matchKey.<p>
     * No description.
     */
    public String getMatchKey() {
        return matchKey;
    }

    /**
     * Setter for matchKey.<p>
     * No description.
     */
    public void setMatchKey(String matchKey) {
        this.matchKey = matchKey;
    }

    /**
     * Getter for matchLevel.<p>
     * No description.
     */
    public Integer getMatchLevel() {
        return matchLevel;
    }

    /**
     * Setter for matchLevel.<p>
     * No description.
     */
    public void setMatchLevel(Integer matchLevel) {
        this.matchLevel = matchLevel;
    }

    /**
     * Getter for matchLevelCode.<p>
     * No description.
     */
    public String getMatchLevelCode() {
        return matchLevelCode;
    }

    /**
     * Setter for matchLevelCode.<p>
     * No description.
     */
    public void setMatchLevelCode(String matchLevelCode) {
        this.matchLevelCode = matchLevelCode;
    }

    /**
     * Getter for matchScores.<p>
     * No description.
     */
    public MatchScores getMatchScores() {
        return matchScores;
    }

    /**
     * Setter for matchScores.<p>
     * No description.
     */
    public void setMatchScores(MatchScores matchScores) {
        this.matchScores = matchScores;
    }

    /**
     * Getter for records.<p>
     * No description.
     */
    public Records getRecords() {
        return records;
    }

    /**
     * Setter for records.<p>
     * No description.
     */
    public void setRecords(Records records) {
        this.records = records;
    }

    /**
     * Getter for recordSummary.<p>
     * No description.
     */
    public RecordSummary getRecordSummary() {
        return recordSummary;
    }

    /**
     * Setter for recordSummary.<p>
     * No description.
     */
    public void setRecordSummary(RecordSummary recordSummary) {
        this.recordSummary = recordSummary;
    }
}
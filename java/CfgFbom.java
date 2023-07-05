// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class CfgFbom {
    @JsonProperty("DERIVED")
    private String derived;

    @JsonProperty("DISPLAY_DELIM")
    private String displayDelim;

    @JsonProperty("DISPLAY_LEVEL")
    private Integer displayLevel;

    @JsonProperty("EXEC_ORDER")
    private Integer execOrder;

    @JsonProperty("FELEM_ID")
    private Integer felemId;

    @JsonProperty("FTYPE_ID")
    private Integer ftypeId;

    public CfgFbom() {
    }

    /**
     * Getter for derived.<p>
     * No description.
     */
    public String getDerived() {
        return derived;
    }

    /**
     * Setter for derived.<p>
     * No description.
     */
    public void setDerived(String derived) {
        this.derived = derived;
    }

    /**
     * Getter for displayDelim.<p>
     * No description.
     */
    public String getDisplayDelim() {
        return displayDelim;
    }

    /**
     * Setter for displayDelim.<p>
     * No description.
     */
    public void setDisplayDelim(String displayDelim) {
        this.displayDelim = displayDelim;
    }

    /**
     * Getter for displayLevel.<p>
     * No description.
     */
    public Integer getDisplayLevel() {
        return displayLevel;
    }

    /**
     * Setter for displayLevel.<p>
     * No description.
     */
    public void setDisplayLevel(Integer displayLevel) {
        this.displayLevel = displayLevel;
    }

    /**
     * Getter for execOrder.<p>
     * No description.
     */
    public Integer getExecOrder() {
        return execOrder;
    }

    /**
     * Setter for execOrder.<p>
     * No description.
     */
    public void setExecOrder(Integer execOrder) {
        this.execOrder = execOrder;
    }

    /**
     * Getter for felemId.<p>
     * No description.
     */
    public Integer getFelemId() {
        return felemId;
    }

    /**
     * Setter for felemId.<p>
     * No description.
     */
    public void setFelemId(Integer felemId) {
        this.felemId = felemId;
    }

    /**
     * Getter for ftypeId.<p>
     * No description.
     */
    public Integer getFtypeId() {
        return ftypeId;
    }

    /**
     * Setter for ftypeId.<p>
     * No description.
     */
    public void setFtypeId(Integer ftypeId) {
        this.ftypeId = ftypeId;
    }
}

// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class CfgFbovr {
    @JsonProperty("ECLASS_ID")
    private Integer eclassId;

    @JsonProperty("FTYPE_EXCL")
    private String ftypeExcl;

    @JsonProperty("FTYPE_FREQ")
    private String ftypeFreq;

    @JsonProperty("FTYPE_ID")
    private Integer ftypeId;

    @JsonProperty("FTYPE_STAB")
    private String ftypeStab;

    @JsonProperty("UTYPE_CODE")
    private String utypeCode;

    public CfgFbovr() {
    }

    /**
     * Getter for eclassId.<p>
     * No description.
     */
    public Integer getEclassId() {
        return eclassId;
    }

    /**
     * Setter for eclassId.<p>
     * No description.
     */
    public void setEclassId(Integer eclassId) {
        this.eclassId = eclassId;
    }

    /**
     * Getter for ftypeExcl.<p>
     * No description.
     */
    public String getFtypeExcl() {
        return ftypeExcl;
    }

    /**
     * Setter for ftypeExcl.<p>
     * No description.
     */
    public void setFtypeExcl(String ftypeExcl) {
        this.ftypeExcl = ftypeExcl;
    }

    /**
     * Getter for ftypeFreq.<p>
     * No description.
     */
    public String getFtypeFreq() {
        return ftypeFreq;
    }

    /**
     * Setter for ftypeFreq.<p>
     * No description.
     */
    public void setFtypeFreq(String ftypeFreq) {
        this.ftypeFreq = ftypeFreq;
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

    /**
     * Getter for ftypeStab.<p>
     * No description.
     */
    public String getFtypeStab() {
        return ftypeStab;
    }

    /**
     * Setter for ftypeStab.<p>
     * No description.
     */
    public void setFtypeStab(String ftypeStab) {
        this.ftypeStab = ftypeStab;
    }

    /**
     * Getter for utypeCode.<p>
     * No description.
     */
    public String getUtypeCode() {
        return utypeCode;
    }

    /**
     * Setter for utypeCode.<p>
     * No description.
     */
    public void setUtypeCode(String utypeCode) {
        this.utypeCode = utypeCode;
    }
}

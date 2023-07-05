// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class CfgErrule {
    @JsonProperty("DISQ_ERFRAG_CODE")
    private String disqErfragCode;

    @JsonProperty("ERRULE_CODE")
    private String erruleCode;

    @JsonProperty("ERRULE_DESC")
    private String erruleDesc;

    @JsonProperty("ERRULE_ID")
    private Integer erruleId;

    @JsonProperty("ERRULE_TIER")
    private Integer erruleTier;

    @JsonProperty("QUAL_ERFRAG_CODE")
    private String qualErfragCode;

    @JsonProperty("REF_SCORE")
    private Integer refScore;

    @JsonProperty("RELATE")
    private String relate;

    @JsonProperty("RESOLVE")
    private String resolve;

    @JsonProperty("RTYPE_ID")
    private Integer rtypeId;

    public CfgErrule() {
    }

    /**
     * Getter for disqErfragCode.<p>
     * No description.
     */
    public String getDisqErfragCode() {
        return disqErfragCode;
    }

    /**
     * Setter for disqErfragCode.<p>
     * No description.
     */
    public void setDisqErfragCode(String disqErfragCode) {
        this.disqErfragCode = disqErfragCode;
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
     * Getter for erruleDesc.<p>
     * No description.
     */
    public String getErruleDesc() {
        return erruleDesc;
    }

    /**
     * Setter for erruleDesc.<p>
     * No description.
     */
    public void setErruleDesc(String erruleDesc) {
        this.erruleDesc = erruleDesc;
    }

    /**
     * Getter for erruleId.<p>
     * No description.
     */
    public Integer getErruleId() {
        return erruleId;
    }

    /**
     * Setter for erruleId.<p>
     * No description.
     */
    public void setErruleId(Integer erruleId) {
        this.erruleId = erruleId;
    }

    /**
     * Getter for erruleTier.<p>
     * No description.
     */
    public Integer getErruleTier() {
        return erruleTier;
    }

    /**
     * Setter for erruleTier.<p>
     * No description.
     */
    public void setErruleTier(Integer erruleTier) {
        this.erruleTier = erruleTier;
    }

    /**
     * Getter for qualErfragCode.<p>
     * No description.
     */
    public String getQualErfragCode() {
        return qualErfragCode;
    }

    /**
     * Setter for qualErfragCode.<p>
     * No description.
     */
    public void setQualErfragCode(String qualErfragCode) {
        this.qualErfragCode = qualErfragCode;
    }

    /**
     * Getter for refScore.<p>
     * No description.
     */
    public Integer getRefScore() {
        return refScore;
    }

    /**
     * Setter for refScore.<p>
     * No description.
     */
    public void setRefScore(Integer refScore) {
        this.refScore = refScore;
    }

    /**
     * Getter for relate.<p>
     * No description.
     */
    public String getRelate() {
        return relate;
    }

    /**
     * Setter for relate.<p>
     * No description.
     */
    public void setRelate(String relate) {
        this.relate = relate;
    }

    /**
     * Getter for resolve.<p>
     * No description.
     */
    public String getResolve() {
        return resolve;
    }

    /**
     * Setter for resolve.<p>
     * No description.
     */
    public void setResolve(String resolve) {
        this.resolve = resolve;
    }

    /**
     * Getter for rtypeId.<p>
     * No description.
     */
    public Integer getRtypeId() {
        return rtypeId;
    }

    /**
     * Setter for rtypeId.<p>
     * No description.
     */
    public void setRtypeId(Integer rtypeId) {
        this.rtypeId = rtypeId;
    }
}
// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

@JsonSerialize
public class G2diagnosticGetMappingStatisticsResponse0 {
    @JsonProperty("DERIVED")
    private String derived;

    @JsonProperty("DSRC_CODE")
    private String dsrcCode;

    @JsonProperty("ETYPE_CODE")
    private String etypeCode;

    @JsonProperty("FTYPE_CODE")
    private String ftypeCode;

    @JsonProperty("MAX_FEAT_DESC")
    private String maxFeatDesc;

    @JsonProperty("MIN_FEAT_DESC")
    private String minFeatDesc;

    @JsonProperty("REC_COUNT")
    private Integer recCount;

    @JsonProperty("REC_PCT")
    private Double recPct;

    @JsonProperty("UNIQ_COUNT")
    private Integer uniqCount;

    @JsonProperty("UNIQ_PCT")
    private Double uniqPct;

    @JsonProperty("USAGE_TYPE")
    private String usageType;

    public G2diagnosticGetMappingStatisticsResponse0() {
    }

    /**
     * Getter for derived.<p>
     */
    public String getDerived() {
        return derived;
    }

    /**
     * Setter for derived.<p>
     */
    public void setDerived(String derived) {
        this.derived = derived;
    }

    /**
     * Getter for dsrcCode.<p>
     */
    public String getDsrcCode() {
        return dsrcCode;
    }

    /**
     * Setter for dsrcCode.<p>
     */
    public void setDsrcCode(String dsrcCode) {
        this.dsrcCode = dsrcCode;
    }

    /**
     * Getter for etypeCode.<p>
     */
    public String getEtypeCode() {
        return etypeCode;
    }

    /**
     * Setter for etypeCode.<p>
     */
    public void setEtypeCode(String etypeCode) {
        this.etypeCode = etypeCode;
    }

    /**
     * Getter for ftypeCode.<p>
     */
    public String getFtypeCode() {
        return ftypeCode;
    }

    /**
     * Setter for ftypeCode.<p>
     */
    public void setFtypeCode(String ftypeCode) {
        this.ftypeCode = ftypeCode;
    }

    /**
     * Getter for maxFeatDesc.<p>
     */
    public String getMaxFeatDesc() {
        return maxFeatDesc;
    }

    /**
     * Setter for maxFeatDesc.<p>
     */
    public void setMaxFeatDesc(String maxFeatDesc) {
        this.maxFeatDesc = maxFeatDesc;
    }

    /**
     * Getter for minFeatDesc.<p>
     */
    public String getMinFeatDesc() {
        return minFeatDesc;
    }

    /**
     * Setter for minFeatDesc.<p>
     */
    public void setMinFeatDesc(String minFeatDesc) {
        this.minFeatDesc = minFeatDesc;
    }

    /**
     * Getter for recCount.<p>
     */
    public Integer getRecCount() {
        return recCount;
    }

    /**
     * Setter for recCount.<p>
     */
    public void setRecCount(Integer recCount) {
        this.recCount = recCount;
    }

    /**
     * Getter for recPct.<p>
     */
    public Double getRecPct() {
        return recPct;
    }

    /**
     * Setter for recPct.<p>
     */
    public void setRecPct(Double recPct) {
        this.recPct = recPct;
    }

    /**
     * Getter for uniqCount.<p>
     */
    public Integer getUniqCount() {
        return uniqCount;
    }

    /**
     * Setter for uniqCount.<p>
     */
    public void setUniqCount(Integer uniqCount) {
        this.uniqCount = uniqCount;
    }

    /**
     * Getter for uniqPct.<p>
     */
    public Double getUniqPct() {
        return uniqPct;
    }

    /**
     * Setter for uniqPct.<p>
     */
    public void setUniqPct(Double uniqPct) {
        this.uniqPct = uniqPct;
    }

    /**
     * Getter for usageType.<p>
     */
    public String getUsageType() {
        return usageType;
    }

    /**
     * Setter for usageType.<p>
     */
    public void setUsageType(String usageType) {
        this.usageType = usageType;
    }
}
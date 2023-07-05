// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class EngineStatsResponseWorkloadUnresolveTriggers {
    @JsonProperty("ambiguousMultiResolve")
    private Integer ambiguousMultiResolve;

    @JsonProperty("ambiguousNoResolve")
    private Integer ambiguousNoResolve;

    @JsonProperty("extensiveResolve")
    private Integer extensiveResolve;

    @JsonProperty("normalResolve")
    private Integer normalResolve;

    @JsonProperty("relLink")
    private Integer relLink;

    @JsonProperty("update")
    private Integer update;

    public EngineStatsResponseWorkloadUnresolveTriggers() {
    }

    /**
     * Getter for ambiguousMultiResolve.<p>
     * No description.
     */
    public Integer getAmbiguousMultiResolve() {
        return ambiguousMultiResolve;
    }

    /**
     * Setter for ambiguousMultiResolve.<p>
     * No description.
     */
    public void setAmbiguousMultiResolve(Integer ambiguousMultiResolve) {
        this.ambiguousMultiResolve = ambiguousMultiResolve;
    }

    /**
     * Getter for ambiguousNoResolve.<p>
     * No description.
     */
    public Integer getAmbiguousNoResolve() {
        return ambiguousNoResolve;
    }

    /**
     * Setter for ambiguousNoResolve.<p>
     * No description.
     */
    public void setAmbiguousNoResolve(Integer ambiguousNoResolve) {
        this.ambiguousNoResolve = ambiguousNoResolve;
    }

    /**
     * Getter for extensiveResolve.<p>
     * No description.
     */
    public Integer getExtensiveResolve() {
        return extensiveResolve;
    }

    /**
     * Setter for extensiveResolve.<p>
     * No description.
     */
    public void setExtensiveResolve(Integer extensiveResolve) {
        this.extensiveResolve = extensiveResolve;
    }

    /**
     * Getter for normalResolve.<p>
     * No description.
     */
    public Integer getNormalResolve() {
        return normalResolve;
    }

    /**
     * Setter for normalResolve.<p>
     * No description.
     */
    public void setNormalResolve(Integer normalResolve) {
        this.normalResolve = normalResolve;
    }

    /**
     * Getter for relLink.<p>
     * No description.
     */
    public Integer getRelLink() {
        return relLink;
    }

    /**
     * Setter for relLink.<p>
     * No description.
     */
    public void setRelLink(Integer relLink) {
        this.relLink = relLink;
    }

    /**
     * Getter for update.<p>
     * No description.
     */
    public Integer getUpdate() {
        return update;
    }

    /**
     * Setter for update.<p>
     * No description.
     */
    public void setUpdate(Integer update) {
        this.update = update;
    }
}

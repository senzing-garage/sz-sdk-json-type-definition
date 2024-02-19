// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

@JsonSerialize
public class G2engineStatsResponseUnresolveTriggers {
    @JsonProperty("extensiveResolve")
    private Integer extensiveResolve;

    @JsonProperty("normalResolve")
    private Integer normalResolve;

    public G2engineStatsResponseUnresolveTriggers() {
    }

    /**
     * Getter for extensiveResolve.<p>
     */
    public Integer getExtensiveResolve() {
        return extensiveResolve;
    }

    /**
     * Setter for extensiveResolve.<p>
     */
    public void setExtensiveResolve(Integer extensiveResolve) {
        this.extensiveResolve = extensiveResolve;
    }

    /**
     * Getter for normalResolve.<p>
     */
    public Integer getNormalResolve() {
        return normalResolve;
    }

    /**
     * Setter for normalResolve.<p>
     */
    public void setNormalResolve(Integer normalResolve) {
        this.normalResolve = normalResolve;
    }
}
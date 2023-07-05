// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class Config {
    @JsonProperty("CONFIG_COMMENTS")
    private String configComments;

    @JsonProperty("CONFIG_ID")
    private Integer configId;

    @JsonProperty("SYS_CREATE_DT")
    private String sysCreateDt;

    public Config() {
    }

    /**
     * Getter for configComments.<p>
     * No description.
     */
    public String getConfigComments() {
        return configComments;
    }

    /**
     * Setter for configComments.<p>
     * No description.
     */
    public void setConfigComments(String configComments) {
        this.configComments = configComments;
    }

    /**
     * Getter for configId.<p>
     * No description.
     */
    public Integer getConfigId() {
        return configId;
    }

    /**
     * Setter for configId.<p>
     * No description.
     */
    public void setConfigId(Integer configId) {
        this.configId = configId;
    }

    /**
     * Getter for sysCreateDt.<p>
     * No description.
     */
    public String getSysCreateDt() {
        return sysCreateDt;
    }

    /**
     * Setter for sysCreateDt.<p>
     * No description.
     */
    public void setSysCreateDt(String sysCreateDt) {
        this.sysCreateDt = sysCreateDt;
    }
}

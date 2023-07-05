// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * No description.
 */
@JsonSerialize
public class CfgRclass {
    @JsonProperty("IS_DISCLOSED")
    private String isDisclosed;

    @JsonProperty("RCLASS_CODE")
    private String rclassCode;

    @JsonProperty("RCLASS_DESC")
    private String rclassDesc;

    @JsonProperty("RCLASS_ID")
    private Integer rclassId;

    public CfgRclass() {
    }

    /**
     * Getter for isDisclosed.<p>
     * No description.
     */
    public String getIsDisclosed() {
        return isDisclosed;
    }

    /**
     * Setter for isDisclosed.<p>
     * No description.
     */
    public void setIsDisclosed(String isDisclosed) {
        this.isDisclosed = isDisclosed;
    }

    /**
     * Getter for rclassCode.<p>
     * No description.
     */
    public String getRclassCode() {
        return rclassCode;
    }

    /**
     * Setter for rclassCode.<p>
     * No description.
     */
    public void setRclassCode(String rclassCode) {
        this.rclassCode = rclassCode;
    }

    /**
     * Getter for rclassDesc.<p>
     * No description.
     */
    public String getRclassDesc() {
        return rclassDesc;
    }

    /**
     * Setter for rclassDesc.<p>
     * No description.
     */
    public void setRclassDesc(String rclassDesc) {
        this.rclassDesc = rclassDesc;
    }

    /**
     * Getter for rclassId.<p>
     * No description.
     */
    public Integer getRclassId() {
        return rclassId;
    }

    /**
     * Setter for rclassId.<p>
     * No description.
     */
    public void setRclassId(Integer rclassId) {
        this.rclassId = rclassId;
    }
}

// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

@JsonSerialize
public class RegisterDataSource {
    @JsonProperty("DSRC_ID")
    private Integer dsrcId;

    public RegisterDataSource() {
    }

    /**
     * Getter for dsrcId.<p>
     */
    public Integer getDsrcId() {
        return dsrcId;
    }

    /**
     * Setter for dsrcId.<p>
     */
    public void setDsrcId(Integer dsrcId) {
        this.dsrcId = dsrcId;
    }
}

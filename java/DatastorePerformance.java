// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

@JsonSerialize
public class DatastorePerformance {
    @JsonProperty("insertTime")
    private Integer insertTime;

    @JsonProperty("numRecordsInserted")
    private Integer numRecordsInserted;

    public DatastorePerformance() {
    }

    /**
     * Getter for insertTime.<p>
     */
    public Integer getInsertTime() {
        return insertTime;
    }

    /**
     * Setter for insertTime.<p>
     */
    public void setInsertTime(Integer insertTime) {
        this.insertTime = insertTime;
    }

    /**
     * Getter for numRecordsInserted.<p>
     */
    public Integer getNumRecordsInserted() {
        return numRecordsInserted;
    }

    /**
     * Setter for numRecordsInserted.<p>
     */
    public void setNumRecordsInserted(Integer numRecordsInserted) {
        this.numRecordsInserted = numRecordsInserted;
    }
}
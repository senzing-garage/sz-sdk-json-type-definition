// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import java.util.List;

@JsonSerialize
public class DatastoreInfo {
    @JsonProperty("dataStores")
    private List<Datastore> dataStores;

    public DatastoreInfo() {
    }

    /**
     * Getter for dataStores.<p>
     */
    public List<Datastore> getDataStores() {
        return dataStores;
    }

    /**
     * Setter for dataStores.<p>
     */
    public void setDataStores(List<Datastore> dataStores) {
        this.dataStores = dataStores;
    }
}
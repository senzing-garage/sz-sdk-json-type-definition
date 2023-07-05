// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

@JsonSerialize
public class EngineStatsResponseWorkloadSystemResourcesCurrResourceSystemLoad {
    @JsonProperty("cpuIdle")
    private Double cpuIdle;

    @JsonProperty("cpuSoftIrq")
    private Double cpuSoftIrq;

    @JsonProperty("cpuSystem")
    private Double cpuSystem;

    @JsonProperty("cpuUser")
    private Double cpuUser;

    @JsonProperty("cpuWait")
    private Double cpuWait;

    public EngineStatsResponseWorkloadSystemResourcesCurrResourceSystemLoad() {
    }

    /**
     * Getter for cpuIdle.<p>
     * No description.
     */
    public Double getCpuIdle() {
        return cpuIdle;
    }

    /**
     * Setter for cpuIdle.<p>
     * No description.
     */
    public void setCpuIdle(Double cpuIdle) {
        this.cpuIdle = cpuIdle;
    }

    /**
     * Getter for cpuSoftIrq.<p>
     * No description.
     */
    public Double getCpuSoftIrq() {
        return cpuSoftIrq;
    }

    /**
     * Setter for cpuSoftIrq.<p>
     * No description.
     */
    public void setCpuSoftIrq(Double cpuSoftIrq) {
        this.cpuSoftIrq = cpuSoftIrq;
    }

    /**
     * Getter for cpuSystem.<p>
     * No description.
     */
    public Double getCpuSystem() {
        return cpuSystem;
    }

    /**
     * Setter for cpuSystem.<p>
     * No description.
     */
    public void setCpuSystem(Double cpuSystem) {
        this.cpuSystem = cpuSystem;
    }

    /**
     * Getter for cpuUser.<p>
     * No description.
     */
    public Double getCpuUser() {
        return cpuUser;
    }

    /**
     * Setter for cpuUser.<p>
     * No description.
     */
    public void setCpuUser(Double cpuUser) {
        this.cpuUser = cpuUser;
    }

    /**
     * Getter for cpuWait.<p>
     * No description.
     */
    public Double getCpuWait() {
        return cpuWait;
    }

    /**
     * Setter for cpuWait.<p>
     * No description.
     */
    public void setCpuWait(Double cpuWait) {
        this.cpuWait = cpuWait;
    }
}

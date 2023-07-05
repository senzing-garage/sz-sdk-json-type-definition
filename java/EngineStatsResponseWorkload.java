// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.senzing.schema;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import java.util.List;

/**
 * No description.
 */
@JsonSerialize
public class EngineStatsResponseWorkload {
    @JsonProperty("CorruptEntityTestDiagnosis")
    private Object corruptEntityTestDiagnosis;

    @JsonProperty("abortedUnresolve")
    private Integer abortedUnresolve;

    @JsonProperty("actualAmbiguousTest")
    private Integer actualAmbiguousTest;

    @JsonProperty("addedRecords")
    private Integer addedRecords;

    @JsonProperty("apiVersion")
    private String apiVersion;

    @JsonProperty("cacheHit")
    private AttributeCounters cacheHit;

    @JsonProperty("cacheMiss")
    private AttributeCounters cacheMiss;

    @JsonProperty("cachedAmbiguousTest")
    private Integer cachedAmbiguousTest;

    @JsonProperty("candidateBuilders")
    private AttributeCounters candidateBuilders;

    @JsonProperty("candidates")
    private Integer candidates;

    @JsonProperty("deletedRecords")
    private Integer deletedRecords;

    @JsonProperty("duration")
    private Integer duration;

    @JsonProperty("expressedFeatureCalls")
    private List<EngineStatsResponseWorkloadExpressedFeatureCall> expressedFeatureCalls;

    @JsonProperty("expressedFeaturesCreated")
    private AttributeCounters expressedFeaturesCreated;

    @JsonProperty("filteredObsFeat")
    private Integer filteredObsFeat;

    @JsonProperty("genericDetect")
    private AttributeCounters genericDetect;

    @JsonProperty("gnrScorersUsed")
    private Integer gnrScorersUsed;

    @JsonProperty("highContentionFeat")
    private AttributeCounters highContentionFeat;

    @JsonProperty("highContentionResEnt")
    private AttributeCounters highContentionResEnt;

    @JsonProperty("latchContention")
    private AttributeCounters latchContention;

    @JsonProperty("libFeatCacheHit")
    private Integer libFeatCacheHit;

    @JsonProperty("libFeatCacheMiss")
    private Integer libFeatCacheMiss;

    @JsonProperty("loadedRecords")
    private Integer loadedRecords;

    @JsonProperty("redoTriggers")
    private AttributeCounters redoTriggers;

    @JsonProperty("reducedScoredFeatureType")
    private AttributeCounters reducedScoredFeatureType;

    @JsonProperty("reevaluations")
    private Integer reevaluations;

    @JsonProperty("repairedEntities")
    private Integer repairedEntities;

    @JsonProperty("reresolveSkipped")
    private Integer reresolveSkipped;

    @JsonProperty("reresolveTriggers")
    private EngineStatsResponseWorkloadReresolveTriggers reresolveTriggers;

    @JsonProperty("resFeatStatCacheHit")
    private Integer resFeatStatCacheHit;

    @JsonProperty("resFeatStatCacheMiss")
    private Integer resFeatStatCacheMiss;

    @JsonProperty("resFeatStatUpdate")
    private Integer resFeatStatUpdate;

    @JsonProperty("retries")
    private Integer retries;

    @JsonProperty("scoredPairs")
    private AttributeCounters scoredPairs;

    @JsonProperty("suppressedCandidateBuilders")
    private AttributeCounters suppressedCandidateBuilders;

    @JsonProperty("suppressedDisclosedRelationshipDomainCount")
    private Integer suppressedDisclosedRelationshipDomainCount;

    @JsonProperty("suppressedScoredFeatureType")
    private AttributeCounters suppressedScoredFeatureType;

    @JsonProperty("systemResources")
    private EngineStatsResponseWorkloadSystemResources systemResources;

    @JsonProperty("threadState")
    private EngineStatsResponseWorkloadThreadState threadState;

    @JsonProperty("unresolveTest")
    private Integer unresolveTest;

    @JsonProperty("unresolveTriggers")
    private EngineStatsResponseWorkloadUnresolveTriggers unresolveTriggers;

    public EngineStatsResponseWorkload() {
    }

    /**
     * Getter for corruptEntityTestDiagnosis.<p>
     * No description.
     */
    public Object getCorruptEntityTestDiagnosis() {
        return corruptEntityTestDiagnosis;
    }

    /**
     * Setter for corruptEntityTestDiagnosis.<p>
     * No description.
     */
    public void setCorruptEntityTestDiagnosis(Object corruptEntityTestDiagnosis) {
        this.corruptEntityTestDiagnosis = corruptEntityTestDiagnosis;
    }

    /**
     * Getter for abortedUnresolve.<p>
     * No description.
     */
    public Integer getAbortedUnresolve() {
        return abortedUnresolve;
    }

    /**
     * Setter for abortedUnresolve.<p>
     * No description.
     */
    public void setAbortedUnresolve(Integer abortedUnresolve) {
        this.abortedUnresolve = abortedUnresolve;
    }

    /**
     * Getter for actualAmbiguousTest.<p>
     * No description.
     */
    public Integer getActualAmbiguousTest() {
        return actualAmbiguousTest;
    }

    /**
     * Setter for actualAmbiguousTest.<p>
     * No description.
     */
    public void setActualAmbiguousTest(Integer actualAmbiguousTest) {
        this.actualAmbiguousTest = actualAmbiguousTest;
    }

    /**
     * Getter for addedRecords.<p>
     * No description.
     */
    public Integer getAddedRecords() {
        return addedRecords;
    }

    /**
     * Setter for addedRecords.<p>
     * No description.
     */
    public void setAddedRecords(Integer addedRecords) {
        this.addedRecords = addedRecords;
    }

    /**
     * Getter for apiVersion.<p>
     * No description.
     */
    public String getApiVersion() {
        return apiVersion;
    }

    /**
     * Setter for apiVersion.<p>
     * No description.
     */
    public void setApiVersion(String apiVersion) {
        this.apiVersion = apiVersion;
    }

    /**
     * Getter for cacheHit.<p>
     * No description.
     */
    public AttributeCounters getCacheHit() {
        return cacheHit;
    }

    /**
     * Setter for cacheHit.<p>
     * No description.
     */
    public void setCacheHit(AttributeCounters cacheHit) {
        this.cacheHit = cacheHit;
    }

    /**
     * Getter for cacheMiss.<p>
     * No description.
     */
    public AttributeCounters getCacheMiss() {
        return cacheMiss;
    }

    /**
     * Setter for cacheMiss.<p>
     * No description.
     */
    public void setCacheMiss(AttributeCounters cacheMiss) {
        this.cacheMiss = cacheMiss;
    }

    /**
     * Getter for cachedAmbiguousTest.<p>
     * No description.
     */
    public Integer getCachedAmbiguousTest() {
        return cachedAmbiguousTest;
    }

    /**
     * Setter for cachedAmbiguousTest.<p>
     * No description.
     */
    public void setCachedAmbiguousTest(Integer cachedAmbiguousTest) {
        this.cachedAmbiguousTest = cachedAmbiguousTest;
    }

    /**
     * Getter for candidateBuilders.<p>
     * No description.
     */
    public AttributeCounters getCandidateBuilders() {
        return candidateBuilders;
    }

    /**
     * Setter for candidateBuilders.<p>
     * No description.
     */
    public void setCandidateBuilders(AttributeCounters candidateBuilders) {
        this.candidateBuilders = candidateBuilders;
    }

    /**
     * Getter for candidates.<p>
     * No description.
     */
    public Integer getCandidates() {
        return candidates;
    }

    /**
     * Setter for candidates.<p>
     * No description.
     */
    public void setCandidates(Integer candidates) {
        this.candidates = candidates;
    }

    /**
     * Getter for deletedRecords.<p>
     * No description.
     */
    public Integer getDeletedRecords() {
        return deletedRecords;
    }

    /**
     * Setter for deletedRecords.<p>
     * No description.
     */
    public void setDeletedRecords(Integer deletedRecords) {
        this.deletedRecords = deletedRecords;
    }

    /**
     * Getter for duration.<p>
     * No description.
     */
    public Integer getDuration() {
        return duration;
    }

    /**
     * Setter for duration.<p>
     * No description.
     */
    public void setDuration(Integer duration) {
        this.duration = duration;
    }

    /**
     * Getter for expressedFeatureCalls.<p>
     * No description.
     */
    public List<EngineStatsResponseWorkloadExpressedFeatureCall> getExpressedFeatureCalls() {
        return expressedFeatureCalls;
    }

    /**
     * Setter for expressedFeatureCalls.<p>
     * No description.
     */
    public void setExpressedFeatureCalls(List<EngineStatsResponseWorkloadExpressedFeatureCall> expressedFeatureCalls) {
        this.expressedFeatureCalls = expressedFeatureCalls;
    }

    /**
     * Getter for expressedFeaturesCreated.<p>
     * No description.
     */
    public AttributeCounters getExpressedFeaturesCreated() {
        return expressedFeaturesCreated;
    }

    /**
     * Setter for expressedFeaturesCreated.<p>
     * No description.
     */
    public void setExpressedFeaturesCreated(AttributeCounters expressedFeaturesCreated) {
        this.expressedFeaturesCreated = expressedFeaturesCreated;
    }

    /**
     * Getter for filteredObsFeat.<p>
     * No description.
     */
    public Integer getFilteredObsFeat() {
        return filteredObsFeat;
    }

    /**
     * Setter for filteredObsFeat.<p>
     * No description.
     */
    public void setFilteredObsFeat(Integer filteredObsFeat) {
        this.filteredObsFeat = filteredObsFeat;
    }

    /**
     * Getter for genericDetect.<p>
     * No description.
     */
    public AttributeCounters getGenericDetect() {
        return genericDetect;
    }

    /**
     * Setter for genericDetect.<p>
     * No description.
     */
    public void setGenericDetect(AttributeCounters genericDetect) {
        this.genericDetect = genericDetect;
    }

    /**
     * Getter for gnrScorersUsed.<p>
     * No description.
     */
    public Integer getGnrScorersUsed() {
        return gnrScorersUsed;
    }

    /**
     * Setter for gnrScorersUsed.<p>
     * No description.
     */
    public void setGnrScorersUsed(Integer gnrScorersUsed) {
        this.gnrScorersUsed = gnrScorersUsed;
    }

    /**
     * Getter for highContentionFeat.<p>
     * No description.
     */
    public AttributeCounters getHighContentionFeat() {
        return highContentionFeat;
    }

    /**
     * Setter for highContentionFeat.<p>
     * No description.
     */
    public void setHighContentionFeat(AttributeCounters highContentionFeat) {
        this.highContentionFeat = highContentionFeat;
    }

    /**
     * Getter for highContentionResEnt.<p>
     * No description.
     */
    public AttributeCounters getHighContentionResEnt() {
        return highContentionResEnt;
    }

    /**
     * Setter for highContentionResEnt.<p>
     * No description.
     */
    public void setHighContentionResEnt(AttributeCounters highContentionResEnt) {
        this.highContentionResEnt = highContentionResEnt;
    }

    /**
     * Getter for latchContention.<p>
     * No description.
     */
    public AttributeCounters getLatchContention() {
        return latchContention;
    }

    /**
     * Setter for latchContention.<p>
     * No description.
     */
    public void setLatchContention(AttributeCounters latchContention) {
        this.latchContention = latchContention;
    }

    /**
     * Getter for libFeatCacheHit.<p>
     * No description.
     */
    public Integer getLibFeatCacheHit() {
        return libFeatCacheHit;
    }

    /**
     * Setter for libFeatCacheHit.<p>
     * No description.
     */
    public void setLibFeatCacheHit(Integer libFeatCacheHit) {
        this.libFeatCacheHit = libFeatCacheHit;
    }

    /**
     * Getter for libFeatCacheMiss.<p>
     * No description.
     */
    public Integer getLibFeatCacheMiss() {
        return libFeatCacheMiss;
    }

    /**
     * Setter for libFeatCacheMiss.<p>
     * No description.
     */
    public void setLibFeatCacheMiss(Integer libFeatCacheMiss) {
        this.libFeatCacheMiss = libFeatCacheMiss;
    }

    /**
     * Getter for loadedRecords.<p>
     * No description.
     */
    public Integer getLoadedRecords() {
        return loadedRecords;
    }

    /**
     * Setter for loadedRecords.<p>
     * No description.
     */
    public void setLoadedRecords(Integer loadedRecords) {
        this.loadedRecords = loadedRecords;
    }

    /**
     * Getter for redoTriggers.<p>
     * No description.
     */
    public AttributeCounters getRedoTriggers() {
        return redoTriggers;
    }

    /**
     * Setter for redoTriggers.<p>
     * No description.
     */
    public void setRedoTriggers(AttributeCounters redoTriggers) {
        this.redoTriggers = redoTriggers;
    }

    /**
     * Getter for reducedScoredFeatureType.<p>
     * No description.
     */
    public AttributeCounters getReducedScoredFeatureType() {
        return reducedScoredFeatureType;
    }

    /**
     * Setter for reducedScoredFeatureType.<p>
     * No description.
     */
    public void setReducedScoredFeatureType(AttributeCounters reducedScoredFeatureType) {
        this.reducedScoredFeatureType = reducedScoredFeatureType;
    }

    /**
     * Getter for reevaluations.<p>
     * No description.
     */
    public Integer getReevaluations() {
        return reevaluations;
    }

    /**
     * Setter for reevaluations.<p>
     * No description.
     */
    public void setReevaluations(Integer reevaluations) {
        this.reevaluations = reevaluations;
    }

    /**
     * Getter for repairedEntities.<p>
     * No description.
     */
    public Integer getRepairedEntities() {
        return repairedEntities;
    }

    /**
     * Setter for repairedEntities.<p>
     * No description.
     */
    public void setRepairedEntities(Integer repairedEntities) {
        this.repairedEntities = repairedEntities;
    }

    /**
     * Getter for reresolveSkipped.<p>
     * No description.
     */
    public Integer getReresolveSkipped() {
        return reresolveSkipped;
    }

    /**
     * Setter for reresolveSkipped.<p>
     * No description.
     */
    public void setReresolveSkipped(Integer reresolveSkipped) {
        this.reresolveSkipped = reresolveSkipped;
    }

    /**
     * Getter for reresolveTriggers.<p>
     * No description.
     */
    public EngineStatsResponseWorkloadReresolveTriggers getReresolveTriggers() {
        return reresolveTriggers;
    }

    /**
     * Setter for reresolveTriggers.<p>
     * No description.
     */
    public void setReresolveTriggers(EngineStatsResponseWorkloadReresolveTriggers reresolveTriggers) {
        this.reresolveTriggers = reresolveTriggers;
    }

    /**
     * Getter for resFeatStatCacheHit.<p>
     * No description.
     */
    public Integer getResFeatStatCacheHit() {
        return resFeatStatCacheHit;
    }

    /**
     * Setter for resFeatStatCacheHit.<p>
     * No description.
     */
    public void setResFeatStatCacheHit(Integer resFeatStatCacheHit) {
        this.resFeatStatCacheHit = resFeatStatCacheHit;
    }

    /**
     * Getter for resFeatStatCacheMiss.<p>
     * No description.
     */
    public Integer getResFeatStatCacheMiss() {
        return resFeatStatCacheMiss;
    }

    /**
     * Setter for resFeatStatCacheMiss.<p>
     * No description.
     */
    public void setResFeatStatCacheMiss(Integer resFeatStatCacheMiss) {
        this.resFeatStatCacheMiss = resFeatStatCacheMiss;
    }

    /**
     * Getter for resFeatStatUpdate.<p>
     * No description.
     */
    public Integer getResFeatStatUpdate() {
        return resFeatStatUpdate;
    }

    /**
     * Setter for resFeatStatUpdate.<p>
     * No description.
     */
    public void setResFeatStatUpdate(Integer resFeatStatUpdate) {
        this.resFeatStatUpdate = resFeatStatUpdate;
    }

    /**
     * Getter for retries.<p>
     * No description.
     */
    public Integer getRetries() {
        return retries;
    }

    /**
     * Setter for retries.<p>
     * No description.
     */
    public void setRetries(Integer retries) {
        this.retries = retries;
    }

    /**
     * Getter for scoredPairs.<p>
     * No description.
     */
    public AttributeCounters getScoredPairs() {
        return scoredPairs;
    }

    /**
     * Setter for scoredPairs.<p>
     * No description.
     */
    public void setScoredPairs(AttributeCounters scoredPairs) {
        this.scoredPairs = scoredPairs;
    }

    /**
     * Getter for suppressedCandidateBuilders.<p>
     * No description.
     */
    public AttributeCounters getSuppressedCandidateBuilders() {
        return suppressedCandidateBuilders;
    }

    /**
     * Setter for suppressedCandidateBuilders.<p>
     * No description.
     */
    public void setSuppressedCandidateBuilders(AttributeCounters suppressedCandidateBuilders) {
        this.suppressedCandidateBuilders = suppressedCandidateBuilders;
    }

    /**
     * Getter for suppressedDisclosedRelationshipDomainCount.<p>
     * No description.
     */
    public Integer getSuppressedDisclosedRelationshipDomainCount() {
        return suppressedDisclosedRelationshipDomainCount;
    }

    /**
     * Setter for suppressedDisclosedRelationshipDomainCount.<p>
     * No description.
     */
    public void setSuppressedDisclosedRelationshipDomainCount(Integer suppressedDisclosedRelationshipDomainCount) {
        this.suppressedDisclosedRelationshipDomainCount = suppressedDisclosedRelationshipDomainCount;
    }

    /**
     * Getter for suppressedScoredFeatureType.<p>
     * No description.
     */
    public AttributeCounters getSuppressedScoredFeatureType() {
        return suppressedScoredFeatureType;
    }

    /**
     * Setter for suppressedScoredFeatureType.<p>
     * No description.
     */
    public void setSuppressedScoredFeatureType(AttributeCounters suppressedScoredFeatureType) {
        this.suppressedScoredFeatureType = suppressedScoredFeatureType;
    }

    /**
     * Getter for systemResources.<p>
     * No description.
     */
    public EngineStatsResponseWorkloadSystemResources getSystemResources() {
        return systemResources;
    }

    /**
     * Setter for systemResources.<p>
     * No description.
     */
    public void setSystemResources(EngineStatsResponseWorkloadSystemResources systemResources) {
        this.systemResources = systemResources;
    }

    /**
     * Getter for threadState.<p>
     * No description.
     */
    public EngineStatsResponseWorkloadThreadState getThreadState() {
        return threadState;
    }

    /**
     * Setter for threadState.<p>
     * No description.
     */
    public void setThreadState(EngineStatsResponseWorkloadThreadState threadState) {
        this.threadState = threadState;
    }

    /**
     * Getter for unresolveTest.<p>
     * No description.
     */
    public Integer getUnresolveTest() {
        return unresolveTest;
    }

    /**
     * Setter for unresolveTest.<p>
     * No description.
     */
    public void setUnresolveTest(Integer unresolveTest) {
        this.unresolveTest = unresolveTest;
    }

    /**
     * Getter for unresolveTriggers.<p>
     * No description.
     */
    public EngineStatsResponseWorkloadUnresolveTriggers getUnresolveTriggers() {
        return unresolveTriggers;
    }

    /**
     * Setter for unresolveTriggers.<p>
     * No description.
     */
    public void setUnresolveTriggers(EngineStatsResponseWorkloadUnresolveTriggers unresolveTriggers) {
        this.unresolveTriggers = unresolveTriggers;
    }
}

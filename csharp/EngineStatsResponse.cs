// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    public class EngineStatsResponse
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("MISSING_RES_ENT")]
        public int MissingResEnt { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("MISSING_RES_ENT_AND_OKEY")]
        public int MissingResEntAndOkey { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("abortedUnresolve")]
        public int AbortedUnresolve { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("actualAmbiguousTest")]
        public int ActualAmbiguousTest { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("addedRecords")]
        public int AddedRecords { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("cacheHit")]
        public AttributeCounters CacheHit { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("candidateBuilders")]
        public AttributeCounters CandidateBuilders { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("candidates")]
        public int Candidates { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("deletedRecords")]
        public int DeletedRecords { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("duration")]
        public EngineStatsResponseDuration Duration { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("filteredObsFeat")]
        public int FilteredObsFeat { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("genericDetect")]
        public AttributeCounters GenericDetect { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("latchContention")]
        public AttributeCounters LatchContention { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("loadedRecords")]
        public int LoadedRecords { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("redoTriggers")]
        public AttributeCounters RedoTriggers { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("reducedScoredFeatureType")]
        public AttributeCounters ReducedScoredFeatureType { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("reevaluations")]
        public int Reevaluations { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("repairedEntities")]
        public int RepairedEntities { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("reresolveSkipped")]
        public int ReresolveSkipped { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("reresolveTriggers")]
        public EngineStatsResponseReresolveTriggers ReresolveTriggers { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("retries")]
        public int Retries { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("scoredPairs")]
        public AttributeCounters ScoredPairs { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("suppressedCandidateBuilders")]
        public AttributeCounters SuppressedCandidateBuilders { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("suppressedScoredFeatureType")]
        public AttributeCounters SuppressedScoredFeatureType { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("unresolveTest")]
        public int UnresolveTest { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("unresolveTriggers")]
        public EngineStatsResponseUnresolveTriggers UnresolveTriggers { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("workload")]
        public EngineStatsResponseWorkload Workload { get; set; }
    }
}

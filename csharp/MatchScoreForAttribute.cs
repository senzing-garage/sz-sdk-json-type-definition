// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    public class MatchScoreForAttribute
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("CANDIDATE_FEAT")]
        public string CandidateFeat { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("FULL_SCORE")]
        public int FullScore { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("GENERATION_MATCH")]
        public int GenerationMatch { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("GNR_FN")]
        public int GnrFn { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("GNR_GN")]
        public int GnrGn { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("GNR_ON")]
        public int GnrOn { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("GNR_SN")]
        public int GnrSn { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("INBOUND_FEAT")]
        public string InboundFeat { get; set; }
    }
}

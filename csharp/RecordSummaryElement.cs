// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    public class RecordSummaryElement
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("DATA_SOURCE")]
        public string DataSource { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("FIRST_SEEN_DT")]
        public string FirstSeenDt { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("LAST_SEEN_DT")]
        public string LastSeenDt { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("RECORD_COUNT")]
        public int RecordCount { get; set; }
    }
}
// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    public class WhyRecords
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("ENTITIES")]
        public Entities Entities { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("WHY_RESULTS")]
        public WhyResults WhyResults { get; set; }
    }
}

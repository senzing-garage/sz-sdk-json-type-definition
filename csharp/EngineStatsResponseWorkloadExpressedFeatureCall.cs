// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    public class EngineStatsResponseWorkloadExpressedFeatureCall
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("EFCALL_ID")]
        public int EfcallId { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("EFUNC_CODE")]
        public string EfuncCode { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("numCalls")]
        public int NumCalls { get; set; }
    }
}

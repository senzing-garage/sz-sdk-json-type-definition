// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    public class CfgFtype
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("ANONYMIZE")]
        public string Anonymize { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("DERIVATION")]
        public string Derivation { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("DERIVED")]
        public string Derived { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("FCLASS_ID")]
        public int FclassId { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("FTYPE_CODE")]
        public string FtypeCode { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("FTYPE_DESC")]
        public string FtypeDesc { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("FTYPE_EXCL")]
        public string FtypeExcl { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("FTYPE_FREQ")]
        public string FtypeFreq { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("FTYPE_ID")]
        public int FtypeId { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("FTYPE_STAB")]
        public string FtypeStab { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("PERSIST_HISTORY")]
        public string PersistHistory { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("RTYPE_ID")]
        public int RtypeId { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("SHOW_IN_MATCH_KEY")]
        public string ShowInMatchKey { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("USED_FOR_CAND")]
        public string UsedForCand { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("VERSION")]
        public int Version_ { get; set; }
    }
}
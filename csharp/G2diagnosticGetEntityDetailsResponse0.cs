// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    public class G2diagnosticGetEntityDetailsResponse0
    {
        [JsonPropertyName("DERIVED")]
        public string Derived { get; set; }

        [JsonPropertyName("DSRC_CODE")]
        public string DsrcCode { get; set; }

        [JsonPropertyName("ERRULE_CODE")]
        public string ErruleCode { get; set; }

        [JsonPropertyName("ETYPE_CODE")]
        public string EtypeCode { get; set; }

        [JsonPropertyName("FEAT_DESC")]
        public string FeatDesc { get; set; }

        [JsonPropertyName("FTYPE_CODE")]
        public string FtypeCode { get; set; }

        [JsonPropertyName("MATCH_KEY")]
        public string MatchKey { get; set; }

        [JsonPropertyName("OBS_ENT_ID")]
        public int ObsEntId { get; set; }

        [JsonPropertyName("RECORD_ID")]
        public int RecordId { get; set; }

        [JsonPropertyName("RES_ENT_ID")]
        public int ResEntId { get; set; }

        [JsonPropertyName("USAGE_TYPE")]
        public string UsageType { get; set; }
    }
}
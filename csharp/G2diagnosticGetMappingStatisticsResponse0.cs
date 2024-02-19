// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    public class G2diagnosticGetMappingStatisticsResponse0
    {
        [JsonPropertyName("DERIVED")]
        public string Derived { get; set; }

        [JsonPropertyName("DSRC_CODE")]
        public string DsrcCode { get; set; }

        [JsonPropertyName("ETYPE_CODE")]
        public string EtypeCode { get; set; }

        [JsonPropertyName("FTYPE_CODE")]
        public string FtypeCode { get; set; }

        [JsonPropertyName("MAX_FEAT_DESC")]
        public string MaxFeatDesc { get; set; }

        [JsonPropertyName("MIN_FEAT_DESC")]
        public string MinFeatDesc { get; set; }

        [JsonPropertyName("REC_COUNT")]
        public int RecCount { get; set; }

        [JsonPropertyName("REC_PCT")]
        public double RecPct { get; set; }

        [JsonPropertyName("UNIQ_COUNT")]
        public int UniqCount { get; set; }

        [JsonPropertyName("UNIQ_PCT")]
        public double UniqPct { get; set; }

        [JsonPropertyName("USAGE_TYPE")]
        public string UsageType { get; set; }
    }
}
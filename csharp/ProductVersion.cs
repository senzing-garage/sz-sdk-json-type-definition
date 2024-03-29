// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    public class ProductVersion
    {
        [JsonPropertyName("BUILD_DATE")]
        public string BuildDate { get; set; }

        [JsonPropertyName("BUILD_NUMBER")]
        public string BuildNumber { get; set; }

        [JsonPropertyName("BUILD_VERSION")]
        public string BuildVersion { get; set; }

        [JsonPropertyName("COMPATIBILITY_VERSION")]
        public CompatibilityVersion CompatibilityVersion { get; set; }

        [JsonPropertyName("PRODUCT_NAME")]
        public string ProductName { get; set; }

        [JsonPropertyName("SCHEMA_VERSION")]
        public SchemaVersion SchemaVersion { get; set; }

        [JsonPropertyName("VERSION")]
        public string Version_ { get; set; }
    }
}
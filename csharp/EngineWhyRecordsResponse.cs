// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    [JsonConverter(typeof(EngineWhyRecordsResponseJsonConverter))]
    public class EngineWhyRecordsResponse
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public WhyRecords Value { get; set; }
    }

    public class EngineWhyRecordsResponseJsonConverter : JsonConverter<EngineWhyRecordsResponse>
    {
        public override EngineWhyRecordsResponse Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new EngineWhyRecordsResponse { Value = JsonSerializer.Deserialize<WhyRecords>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, EngineWhyRecordsResponse value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<WhyRecords>(writer, value.Value, options);
        }
    }
}

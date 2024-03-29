// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    [JsonConverter(typeof(SzConfigGetJsonStringResponseJsonConverter))]
    public class SzConfigGetJsonStringResponse
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public GetJsonString Value { get; set; }
    }

    public class SzConfigGetJsonStringResponseJsonConverter : JsonConverter<SzConfigGetJsonStringResponse>
    {
        public override SzConfigGetJsonStringResponse Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new SzConfigGetJsonStringResponse { Value = JsonSerializer.Deserialize<GetJsonString>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, SzConfigGetJsonStringResponse value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<GetJsonString>(writer, value.Value, options);
        }
    }
}
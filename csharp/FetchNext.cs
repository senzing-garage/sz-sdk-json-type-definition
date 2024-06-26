// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    [JsonConverter(typeof(FetchNextJsonConverter))]
    public class FetchNext
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public FixmeUnknown Value { get; set; }
    }

    public class FetchNextJsonConverter : JsonConverter<FetchNext>
    {
        public override FetchNext Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new FetchNext { Value = JsonSerializer.Deserialize<FixmeUnknown>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, FetchNext value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<FixmeUnknown>(writer, value.Value, options);
        }
    }
}

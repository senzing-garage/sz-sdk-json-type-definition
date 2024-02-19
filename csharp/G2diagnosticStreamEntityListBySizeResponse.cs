// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    [JsonConverter(typeof(G2diagnosticStreamEntityListBySizeResponseJsonConverter))]
    public class G2diagnosticStreamEntityListBySizeResponse
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public FixmeUnknown Value { get; set; }
    }

    public class G2diagnosticStreamEntityListBySizeResponseJsonConverter : JsonConverter<G2diagnosticStreamEntityListBySizeResponse>
    {
        public override G2diagnosticStreamEntityListBySizeResponse Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new G2diagnosticStreamEntityListBySizeResponse { Value = JsonSerializer.Deserialize<FixmeUnknown>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, G2diagnosticStreamEntityListBySizeResponse value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<FixmeUnknown>(writer, value.Value, options);
        }
    }
}
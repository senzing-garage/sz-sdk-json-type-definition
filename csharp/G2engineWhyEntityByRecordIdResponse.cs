// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    [JsonConverter(typeof(G2engineWhyEntityByRecordIdResponseJsonConverter))]
    public class G2engineWhyEntityByRecordIdResponse
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public WhyEntity Value { get; set; }
    }

    public class G2engineWhyEntityByRecordIdResponseJsonConverter : JsonConverter<G2engineWhyEntityByRecordIdResponse>
    {
        public override G2engineWhyEntityByRecordIdResponse Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new G2engineWhyEntityByRecordIdResponse { Value = JsonSerializer.Deserialize<WhyEntity>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, G2engineWhyEntityByRecordIdResponse value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<WhyEntity>(writer, value.Value, options);
        }
    }
}
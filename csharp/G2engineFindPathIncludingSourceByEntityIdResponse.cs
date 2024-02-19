// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    [JsonConverter(typeof(G2engineFindPathIncludingSourceByEntityIdResponseJsonConverter))]
    public class G2engineFindPathIncludingSourceByEntityIdResponse
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public Path Value { get; set; }
    }

    public class G2engineFindPathIncludingSourceByEntityIdResponseJsonConverter : JsonConverter<G2engineFindPathIncludingSourceByEntityIdResponse>
    {
        public override G2engineFindPathIncludingSourceByEntityIdResponse Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new G2engineFindPathIncludingSourceByEntityIdResponse { Value = JsonSerializer.Deserialize<Path>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, G2engineFindPathIncludingSourceByEntityIdResponse value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<Path>(writer, value.Value, options);
        }
    }
}
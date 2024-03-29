// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    [JsonConverter(typeof(SzProductGetVersionResponseJsonConverter))]
    public class SzProductGetVersionResponse
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public ProductVersion Value { get; set; }
    }

    public class SzProductGetVersionResponseJsonConverter : JsonConverter<SzProductGetVersionResponse>
    {
        public override SzProductGetVersionResponse Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new SzProductGetVersionResponse { Value = JsonSerializer.Deserialize<ProductVersion>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, SzProductGetVersionResponse value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<ProductVersion>(writer, value.Value, options);
        }
    }
}
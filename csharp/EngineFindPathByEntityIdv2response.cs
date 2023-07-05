// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    [JsonConverter(typeof(EngineFindPathByEntityIdv2responseJsonConverter))]
    public class EngineFindPathByEntityIdv2response
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public Path Value { get; set; }
    }

    public class EngineFindPathByEntityIdv2responseJsonConverter : JsonConverter<EngineFindPathByEntityIdv2response>
    {
        public override EngineFindPathByEntityIdv2response Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new EngineFindPathByEntityIdv2response { Value = JsonSerializer.Deserialize<Path>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, EngineFindPathByEntityIdv2response value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<Path>(writer, value.Value, options);
        }
    }
}
// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    [JsonConverter(typeof(EngineWhyEntitiesV2responseJsonConverter))]
    public class EngineWhyEntitiesV2response
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public WhyEntities Value { get; set; }
    }

    public class EngineWhyEntitiesV2responseJsonConverter : JsonConverter<EngineWhyEntitiesV2response>
    {
        public override EngineWhyEntitiesV2response Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new EngineWhyEntitiesV2response { Value = JsonSerializer.Deserialize<WhyEntities>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, EngineWhyEntitiesV2response value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<WhyEntities>(writer, value.Value, options);
        }
    }
}

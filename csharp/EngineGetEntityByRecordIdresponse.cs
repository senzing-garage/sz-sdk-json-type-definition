// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    [JsonConverter(typeof(EngineGetEntityByRecordIdresponseJsonConverter))]
    public class EngineGetEntityByRecordIdresponse
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public Entity Value { get; set; }
    }

    public class EngineGetEntityByRecordIdresponseJsonConverter : JsonConverter<EngineGetEntityByRecordIdresponse>
    {
        public override EngineGetEntityByRecordIdresponse Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new EngineGetEntityByRecordIdresponse { Value = JsonSerializer.Deserialize<Entity>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, EngineGetEntityByRecordIdresponse value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<Entity>(writer, value.Value, options);
        }
    }
}

// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    [JsonConverter(typeof(AffectedEntitiesJsonConverter))]
    public class AffectedEntities
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public IList<AffectedEntity> Value { get; set; }
    }

    public class AffectedEntitiesJsonConverter : JsonConverter<AffectedEntities>
    {
        public override AffectedEntities Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new AffectedEntities { Value = JsonSerializer.Deserialize<IList<AffectedEntity>>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, AffectedEntities value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<IList<AffectedEntity>>(writer, value.Value, options);
        }
    }
}

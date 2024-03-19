// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    [JsonConverter(typeof(EntitiesByFeatureIdJsonConverter))]
    public class EntitiesByFeatureId
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public IList<EntityByFeatureId> Value { get; set; }
    }

    public class EntitiesByFeatureIdJsonConverter : JsonConverter<EntitiesByFeatureId>
    {
        public override EntitiesByFeatureId Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new EntitiesByFeatureId { Value = JsonSerializer.Deserialize<IList<EntityByFeatureId>>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, EntitiesByFeatureId value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<IList<EntityByFeatureId>>(writer, value.Value, options);
        }
    }
}
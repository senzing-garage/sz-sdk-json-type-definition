// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    [JsonConverter(typeof(G2diagnosticFindEntitiesByFeatureIdsResponseXxxJsonConverter))]
    public class G2diagnosticFindEntitiesByFeatureIdsResponseXxx
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public IList<G2diagnosticFindEntitiesByFeatureIdsResponseXxx0> Value { get; set; }
    }

    public class G2diagnosticFindEntitiesByFeatureIdsResponseXxxJsonConverter : JsonConverter<G2diagnosticFindEntitiesByFeatureIdsResponseXxx>
    {
        public override G2diagnosticFindEntitiesByFeatureIdsResponseXxx Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new G2diagnosticFindEntitiesByFeatureIdsResponseXxx { Value = JsonSerializer.Deserialize<IList<G2diagnosticFindEntitiesByFeatureIdsResponseXxx0>>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, G2diagnosticFindEntitiesByFeatureIdsResponseXxx value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<IList<G2diagnosticFindEntitiesByFeatureIdsResponseXxx0>>(writer, value.Value, options);
        }
    }
}
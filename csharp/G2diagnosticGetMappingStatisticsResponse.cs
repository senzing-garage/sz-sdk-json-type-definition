// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Senzing
{
    [JsonConverter(typeof(G2diagnosticGetMappingStatisticsResponseJsonConverter))]
    public class G2diagnosticGetMappingStatisticsResponse
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public IList<G2diagnosticGetMappingStatisticsResponse0> Value { get; set; }
    }

    public class G2diagnosticGetMappingStatisticsResponseJsonConverter : JsonConverter<G2diagnosticGetMappingStatisticsResponse>
    {
        public override G2diagnosticGetMappingStatisticsResponse Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new G2diagnosticGetMappingStatisticsResponse { Value = JsonSerializer.Deserialize<IList<G2diagnosticGetMappingStatisticsResponse0>>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, G2diagnosticGetMappingStatisticsResponse value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<IList<G2diagnosticGetMappingStatisticsResponse0>>(writer, value.Value, options);
        }
    }
}
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
    [JsonConverter(typeof(DiagnosticGetDataSourceCountsResponseJsonConverter))]
    public class DiagnosticGetDataSourceCountsResponse
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public IList<DiagnosticGetDataSourceCountsResponse0> Value { get; set; }
    }

    public class DiagnosticGetDataSourceCountsResponseJsonConverter : JsonConverter<DiagnosticGetDataSourceCountsResponse>
    {
        public override DiagnosticGetDataSourceCountsResponse Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new DiagnosticGetDataSourceCountsResponse { Value = JsonSerializer.Deserialize<IList<DiagnosticGetDataSourceCountsResponse0>>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, DiagnosticGetDataSourceCountsResponse value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<IList<DiagnosticGetDataSourceCountsResponse0>>(writer, value.Value, options);
        }
    }
}

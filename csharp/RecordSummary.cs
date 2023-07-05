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
    [JsonConverter(typeof(RecordSummaryJsonConverter))]
    public class RecordSummary
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public IList<RecordSummaryElement> Value { get; set; }
    }

    public class RecordSummaryJsonConverter : JsonConverter<RecordSummary>
    {
        public override RecordSummary Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new RecordSummary { Value = JsonSerializer.Deserialize<IList<RecordSummaryElement>>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, RecordSummary value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<IList<RecordSummaryElement>>(writer, value.Value, options);
        }
    }
}
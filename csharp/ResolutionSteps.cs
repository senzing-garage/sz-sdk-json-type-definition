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
    [JsonConverter(typeof(ResolutionStepsJsonConverter))]
    public class ResolutionSteps
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public IList<ResolutionStep> Value { get; set; }
    }

    public class ResolutionStepsJsonConverter : JsonConverter<ResolutionSteps>
    {
        public override ResolutionSteps Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new ResolutionSteps { Value = JsonSerializer.Deserialize<IList<ResolutionStep>>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, ResolutionSteps value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<IList<ResolutionStep>>(writer, value.Value, options);
        }
    }
}

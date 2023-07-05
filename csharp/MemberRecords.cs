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
    [JsonConverter(typeof(MemberRecordsJsonConverter))]
    public class MemberRecords
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public IList<MemberRecord> Value { get; set; }
    }

    public class MemberRecordsJsonConverter : JsonConverter<MemberRecords>
    {
        public override MemberRecords Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new MemberRecords { Value = JsonSerializer.Deserialize<IList<MemberRecord>>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, MemberRecords value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<IList<MemberRecord>>(writer, value.Value, options);
        }
    }
}

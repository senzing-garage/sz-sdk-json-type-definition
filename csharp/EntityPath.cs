// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Collections.Generic;
using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    public class EntityPath
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("END_ENTITY_ID")]
        public int EndEntityId { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("ENTITIES")]
        public IList<int> Entities { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("START_ENTITY_ID")]
        public int StartEntityId { get; set; }
    }
}
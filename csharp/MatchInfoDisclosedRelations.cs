// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Collections.Generic;
using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    public class MatchInfoDisclosedRelations
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("REL_ANCHOR")]
        public IList<MatchInfoDisclosedRelationsRelAnchor> RelAnchor { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("REL_LINK")]
        public IList<MatchInfoDisclosedRelationsRelLink> RelLink { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("REL_POINTER")]
        public IList<MatchInfoDisclosedRelationsRelPointer> RelPointer { get; set; }
    }
}

// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    public class Relationship
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("RELATIONSHIP_KEY")]
        public string RelationshipKey { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("RELATIONSHIP_TYPE")]
        public string RelationshipType { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("REL_ANCHOR_DOMAIN")]
        public string RelAnchorDomain { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("REL_ANCHOR_KEY")]
        public string RelAnchorKey { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("REL_POINTER_DOMAIN")]
        public string RelPointerDomain { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("REL_POINTER_KEY")]
        public string RelPointerKey { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("REL_POINTER_ROLE")]
        public string RelPointerRole { get; set; }
    }
}
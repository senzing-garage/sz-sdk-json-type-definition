// Code generated by jtd-codegen for C# + System.Text.Json v0.2.1

using System.Text.Json.Serialization;

namespace Senzing
{
    /// <summary>
    /// No description.
    /// </summary>
    public class Phone
    {
        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("PHONE_FROM_DATE")]
        public string PhoneFromDate { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("PHONE_NUMBER")]
        public string PhoneNumber { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("PHONE_THRU_DATE")]
        public string PhoneThruDate { get; set; }

        /// <summary>
        /// No description.
        /// </summary>
        [JsonPropertyName("PHONE_TYPE")]
        public string PhoneType { get; set; }
    }
}
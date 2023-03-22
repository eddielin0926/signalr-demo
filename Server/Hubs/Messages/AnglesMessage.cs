using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class AnglesMessage
    {
        [JsonPropertyName("id")]
        public string? Id { get; set; }
        [JsonPropertyName("timestamp")]
        public string? Timestamp { get; set; }
        [JsonPropertyName("ang1j")]
        public double? Ang1j { get; set; }
        [JsonPropertyName("ang2j")]
        public double? Ang2j { get; set; }
        [JsonPropertyName("ang3j")]
        public double? Ang3j { get; set; }
        [JsonPropertyName("ang4j")]
        public double? Ang4j { get; set; }
        [JsonPropertyName("ang5j")]
        public double? Ang5j { get; set; }
        [JsonPropertyName("ang6j")]
        public double? Ang6j { get; set; }
    }
}

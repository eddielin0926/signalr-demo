using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class StringMessage
    {
        [JsonPropertyName("data")]
        public string? Data { get; set; }
    }
}

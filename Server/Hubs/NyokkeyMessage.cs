using System.Text.Json.Serialization;

namespace Server.Hubs
{
    public class NyokkeyMessage
    {
        [JsonPropertyName("mode")]
        public string? Mode { get; set; }
    }
}
using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PoseStampedMessage
    {
        [JsonPropertyName("header")]
        public HeaderMessage? Header { get; set; }
        [JsonPropertyName("pose")]
        public PoseMessage? Pose { get; set; }
    }
}

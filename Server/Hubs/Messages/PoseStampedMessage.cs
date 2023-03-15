using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PoseStampedMessage
    {
        [JsonPropertyName("header")]
        public HeaderMessage? Header { get; set; }
        [JsonPropertyName("pose")]
        public PoseMessage? Pose { get; set; }
        public PoseStampedMessage(HeaderMessage header, PoseMessage pose)
        {
            Header = header;
            Pose = pose;
        }
    }
}

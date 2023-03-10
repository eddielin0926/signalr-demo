using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PoseStampedMessage
    {
        [JsonPropertyName("header")]
        public HeaderMessage Header;
        [JsonPropertyName("pose")]
        public PoseMessage Pose;
        public PoseStampedMessage(HeaderMessage header, PoseMessage pose)
        {
            Header = header;
            Pose = pose;
        }
    }
}

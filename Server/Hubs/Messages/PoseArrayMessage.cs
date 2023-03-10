using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PoseArrayMessage
    {
        [JsonPropertyName("header")]
        public HeaderMessage Header;
        [JsonPropertyName("poses")]
        public PoseMessage[] Pose;
        public PoseArrayMessage(HeaderMessage header, PoseMessage[] pose)
        {
            Header = header;
            Pose = pose;
        }
    }
}

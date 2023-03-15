using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PoseArrayMessage
    {
        [JsonPropertyName("header")]
        public HeaderMessage? Header { get; set; }
        [JsonPropertyName("poses")]
        public PoseMessage?[] Pose { get; set; }
        public PoseArrayMessage(HeaderMessage header, PoseMessage[] pose)
        {
            Header = header;
            Pose = pose;
        }
    }
}

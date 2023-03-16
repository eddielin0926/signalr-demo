using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PoseMessage
    {
        [JsonPropertyName("position")]
        public PointMessage Position { get; set; }
        [JsonPropertyName("orientation")]
        public QuaternionMessage Orientation { get; set; }
    }
}

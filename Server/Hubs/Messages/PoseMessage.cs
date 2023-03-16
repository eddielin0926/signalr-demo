using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PoseMessage
    {
        [JsonPropertyName("point")]
        public PointMessage? Point { get; set; }
        [JsonPropertyName("quaternion")]
        public QuaternionMessage? Quaternion { get; set; }
    }
}

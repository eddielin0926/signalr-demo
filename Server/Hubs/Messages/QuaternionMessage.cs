using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class QuaternionMessage
    {
        [JsonPropertyName("x")]
        public double? X { get; set; }
        [JsonPropertyName("y")]
        public double? Y { get; set; }
        [JsonPropertyName("z")]
        public double? Z { get; set; }
        [JsonPropertyName("w")]
        public double? W { get; set; }
    }
}

using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PointMessage
    {
        [JsonPropertyName("x")]
        public double? X { get; set; }
        [JsonPropertyName("y")]
        public double? Y { get; set; }
        [JsonPropertyName("z")]
        public double? Z { get; set; }
        public PointMessage(double x, double y, double z)
        {
            X = x;
            Y = y;
            Z = z;
        }
    }
}

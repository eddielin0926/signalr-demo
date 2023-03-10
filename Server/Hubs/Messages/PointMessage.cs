using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PointMessage
    {
        [JsonPropertyName("x")]
        double X;
        [JsonPropertyName("y")]
        double Y;
        [JsonPropertyName("z")]
        double Z;
        public PointMessage(double x, double y, double z)
        {
            X = x;
            Y = y;
            Z = z;
        }
    }
}

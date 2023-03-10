using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class QuaternionMessage
    {
        [JsonPropertyName("x")]
        double X;
        [JsonPropertyName("y")]
        double Y;
        [JsonPropertyName("z")]
        double Z;
        [JsonPropertyName("w")]
        double W;
        public QuaternionMessage(double x, double y, double z, double w)
        {
            X = x;
            Y = y;
            Z = z;
            W = w;
        }
    }
}

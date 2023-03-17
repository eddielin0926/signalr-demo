using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class PoseMessage
    {
        [JsonPropertyName("position")]
<<<<<<< HEAD
        public PointMessage? Position { get; set; }
        [JsonPropertyName("orientation")]
        public QuaternionMessage? Orientation { get; set; }
=======
        public PointMessage Position { get; set; }
        [JsonPropertyName("orientation")]
        public QuaternionMessage Orientation { get; set; }
>>>>>>> e2fe1611020e2248ac772e293cf7f2144e16b15c
    }
}

using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class AnglesMessage
    {
        [JsonPropertyName("id")]
        public string Id;
        [JsonPropertyName("timestamp")]
        public string Timestamp;
        [JsonPropertyName("ang1j")]
        public double Ang1j;
        [JsonPropertyName("ang2j")]
        public double Ang2j;
        [JsonPropertyName("ang3j")]
        public double Ang3j;
        [JsonPropertyName("ang4j")]
        public double Ang4j;
        [JsonPropertyName("ang5j")]
        public double Ang5j;
        [JsonPropertyName("ang6j")]
        public double Ang6j;
        public AnglesMessage(string id, string timestamp, double ang1j, double ang2j, double ang3j, double ang4j, double ang5j, double ang6j)
        {
            Id = id;
            Timestamp = timestamp;
            Ang1j = ang1j;
            Ang2j = ang2j;
            Ang3j = ang3j;
            Ang4j = ang4j;
            Ang5j = ang5j;
            Ang6j = ang6j;
        }
    }
}

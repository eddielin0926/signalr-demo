using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class TimeMessage
    {
        [JsonPropertyName("sec")]
        public int? Sec { get; set; }
        [JsonPropertyName("nsec")]
        public int? Nsec { get; set; }
    }
}

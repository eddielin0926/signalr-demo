using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class TimeMessage
    {
        [JsonPropertyName("secs")]
        public int? Secs { get; set; }
        [JsonPropertyName("nsecs")]
        public int? Nsecs { get; set; }
    }
}

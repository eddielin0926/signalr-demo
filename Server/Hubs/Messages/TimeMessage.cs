using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class TimeMessage
    {
        [JsonPropertyName("sec")]
        int Sec;
        [JsonPropertyName("nsec")]
        int Nsec;
        public TimeMessage(int sec, int nsec)
        {
            Sec = sec;
            Nsec = nsec;
        }
    }
}

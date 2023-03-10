using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class StringMessage
    {
        [JsonPropertyName("data")]
        public string Data;
        public StringMessage(string data)
        {
            Data = data;
        }
    }
}

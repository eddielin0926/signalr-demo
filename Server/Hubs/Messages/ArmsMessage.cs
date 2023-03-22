using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class ArmsMessage
    {
        [JsonPropertyName("arms")]
        public AnglesMessage[]? Arms { get; set; }
    }
}

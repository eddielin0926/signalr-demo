using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class ArmsMessage
    {
        [JsonPropertyName("arms")]
        AnglesMessage[]? Arms { get; set; }
    }
}

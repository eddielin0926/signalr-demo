using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class HeaderMessage
    {
        [JsonPropertyName("seq")]
        public uint? Seq { get; set; }
        [JsonPropertyName("stamp")]
        public TimeMessage? Stamp { get; set; }
        [JsonPropertyName("frame_id")]
        public string? FrameId { get; set; }
    }
}

using System.Text.Json.Serialization;

namespace Server.Hubs.Messages
{
    public class HeaderMessage
    {
        [JsonPropertyName("seq")]
        public uint Seq;
        [JsonPropertyName("stamp")]
        public TimeMessage Stamp;
        [JsonPropertyName("frame_id")]
        public string FrameId;
        public HeaderMessage(uint Seq, TimeMessage Stamp, string frameId)
        {
            this.Seq = Seq;
            this.Stamp = Stamp;
            FrameId = frameId;
        }
    }
}

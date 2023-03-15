using Microsoft.AspNetCore.SignalR;
using Server.Hubs.Messages;
using System.Text.Json.Serialization;

namespace Server.Hubs
{
    public class NyokkeyHub : Hub
    {
        public async Task SendLocation(PoseStampedMessage message)
        {
            await Clients.All.SendAsync("ReceiveLocation", message);
        }
        public async Task SendRightArm(PoseArrayMessage message)
        {
            await Clients.All.SendAsync("ReceiveRightArm", message);
        }
        public async Task SendLeftArm(PoseArrayMessage message)
        {
            await Clients.All.SendAsync("ReceiveLeftArm", message);
        }
        public async Task SendFace(PoseArrayMessage message)
        {
            await Clients.All.SendAsync("ReceiveFace", message);
        }
        public async Task SendTask(StringMessage message)
        {
            await Clients.All.SendAsync("ReceiveTask", message);
        }
    }
}

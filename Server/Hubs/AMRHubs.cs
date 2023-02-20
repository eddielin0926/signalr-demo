using Microsoft.AspNetCore.SignalR;

namespace Server.Hubs
{
    public class AMRHub : Hub
    {
        public async Task SendMessage(string message)
        {
            Console.WriteLine(message);
            await Clients.All.SendAsync("ReceiveMessage", message);
        }
    }
}
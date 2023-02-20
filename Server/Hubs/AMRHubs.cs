using Microsoft.AspNetCore.SignalR;

namespace Server.Hubs
{
    public class AMRHub : Hub
    {
        public async Task SendPosition(string id, string timestamp, string x, string y, string z)
        {
            Console.WriteLine($"receive: id: {id}, timestamp: {timestamp}, x: {x}, y:{y}, z:{z}");
            await Clients.All.SendAsync("ReceiveMessage", id, timestamp, x, y, z);
        }
    }
}
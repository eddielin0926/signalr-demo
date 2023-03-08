using Microsoft.AspNetCore.SignalR;

namespace Server.Hubs
{
    public class RoboticArmHub : Hub
    {
        public async Task SendAngles(string id, string timestamp, double ang1j, double ang2j, double ang3j, double ang4j, double ang5j, double ang6j)
        {
            var message = new RoboticArmMessage
            {
                Id = id,
                Timestamp = timestamp,
                Ang1j = ang1j,
                Ang2j = ang2j,
                Ang3j = ang3j,
                Ang4j = ang4j,
                Ang5j = ang5j,
                Ang6j = ang6j
            };
            Console.WriteLine($"receive: id: {id}, timestamp: {timestamp}, ang1j: {ang1j}, ang2j: {ang2j}, ang3j: {ang3j}, ang4j: {ang4j}, ang5j: {ang5j}, ang6j: {ang6j}");
            await Clients.All.SendAsync("ReceiveMessage", message);
        }
        public async Task SendNyokkey(string mode)
        {
            var message = new NyokkeyMessage{ Mode = mode };
            Console.WriteLine($"receive: mode: {mode}");
            await Clients.All.SendAsync("ReceiveNyokkey", message);
        }
    }
}
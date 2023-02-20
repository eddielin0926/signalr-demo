using Microsoft.AspNetCore.SignalR;

namespace Server.Hubs
{
    public class RoboticArmHub : Hub
    {
        public async Task SendAngles(string id, string timestamp, string ang1j, string ang2j, string ang3j, string ang4j, string ang5j, string ang6j)
        {
            Console.WriteLine($"receive: id: {id}, timestamp: {timestamp}, ang1j: {ang1j}, ang2j: {ang2j}, ang3j: {ang3j}, ang4j: {ang4j}, ang5j: {ang5j}, ang6j: {ang6j}");
            await Clients.All.SendAsync("ReceiveMessage", id, timestamp, ang1j, ang2j, ang3j, ang4j, ang5j, ang6j);
        }
    }
}
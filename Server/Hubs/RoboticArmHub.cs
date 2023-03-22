using Microsoft.AspNetCore.SignalR;
using Server.Hubs.Messages;

namespace Server.Hubs
{
    public class RoboticArmHub : Hub
    {
        public async Task SendAngles(string id, string timestamp, double ang1j, double ang2j, double ang3j, double ang4j, double ang5j, double ang6j)
        {
            var message = new AnglesMessage(id, timestamp, ang1j, ang2j, ang3j, ang4j, ang5j, ang6j);
            Console.WriteLine($"receive ros: id: {id}, timestamp: {timestamp}, ang1j: {ang1j}, ang2j: {ang2j}, ang3j: {ang3j}, ang4j: {ang4j}, ang5j: {ang5j}, ang6j: {ang6j}");
            await Clients.All.SendAsync("ReceiveMessage", message);
        }
        public async Task SendSingleAngles(ArmsMessage message)
        {
            Console.WriteLine(message);
            await Clients.All.SendAsync("ReceiveSingleAngles", message);
        }
    }
}

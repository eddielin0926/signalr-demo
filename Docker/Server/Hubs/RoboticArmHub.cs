using Microsoft.AspNetCore.SignalR;
using System.Text.Json.Serialization;

namespace Server.Hubs
{
    public class RoboticArmMessage
    {
        [JsonPropertyName("id")]
        public string? Id { get; set; }
        [JsonPropertyName("timestamp")]
        public string? Timestamp { get; set; }
        [JsonPropertyName("ang1j")]
        public double? Ang1j { get; set; }
        [JsonPropertyName("ang2j")]
        public double? Ang2j { get; set; }
        [JsonPropertyName("ang3j")]
        public double? Ang3j { get; set; }
        [JsonPropertyName("ang4j")]
        public double? Ang4j { get; set; }
        [JsonPropertyName("ang5j")]
        public double? Ang5j { get; set; }
        [JsonPropertyName("ang6j")]
        public double? Ang6j { get; set; }
    }
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
    }
}

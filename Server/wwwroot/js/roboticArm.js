"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/robotic-arm-hub").build();

var startTime = new Date()
var messageCount = 0;

connection.on("ReceiveMessage", function (message) {
    messageCount += 1;
    var deltaTime = new Date() - startTime;
    var rate = (messageCount * 1000 / deltaTime).toFixed(2);
    document.getElementById("arm-data").innerHTML = `
        Recieved ${messageCount} messages (${rate} msg / sec)
    `;

    var t = document.getElementById(message.id);
    t.innerHTML = `
        <tr id="${message.id}">
            <td>${message.id}</td>
            <td>${message.timestamp}</td>
            <td>${message.ang1j}</td>
            <td>${message.ang2j}</td>
            <td>${message.ang3j}</td>
            <td>${message.ang4j}</td>
            <td>${message.ang5j}</td>
            <td>${message.ang6j}</td>
        </tr>
    `;
});

connection.start().catch(function (err) {
    return console.error(err.toString());
});

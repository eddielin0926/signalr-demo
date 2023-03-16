"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/robotic-arm-hub").build();

connection.on("ReceiveMessage", function (message) {
    console.log(message);
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

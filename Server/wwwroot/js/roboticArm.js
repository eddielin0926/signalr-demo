"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/robotic-arm-hub").build();

//Disable the send button until connection is established.
document.getElementById("sendButton").disabled = true;

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

connection.start().then(function () {
    document.getElementById("sendButton").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("sendButton").addEventListener("click", function (event) {
    var str = document.getElementById("msgInput").value;
    var data = str.split(",");
    var angs = data.slice(-6).map((v) => parseFloat(v));
    if (data) {
        connection.invoke("SendAngles", data[0], data[1], ...angs).catch(function (err) {
            return console.error(err.toString());
        });
    }
    event.preventDefault();
});

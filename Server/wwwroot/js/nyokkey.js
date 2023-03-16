"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/nyokkey").build();

connection.start().catch(function (err) {
    return console.error(err.toString());
});

connection.on("ReceiveLocation", function (message) {
    var t = document.getElementById('location');
    t.innerHTML = `
        <tr id="location">
            <td>/nyokkey/hmi/location</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});

connection.on("ReceiveRightArm", function (message) {
    var t = document.getElementById('rightarm');
    t.innerHTML = `
        <tr id="rightarm">
            <td>/nyokkey/hmi/rightarm</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});

connection.on("ReceiveLeftArm", function (message) {
    var t = document.getElementById('leftarm');
    t.innerHTML = `
        <tr id="leftarm">
            <td>/nyokkey/hmi/leftarm</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});

connection.on("ReceiveFace", function (message) {
    var t = document.getElementById('face');
    t.innerHTML = `
        <tr id="face">
            <td>/nyokkey/hmi/face</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});

connection.on("ReceiveTask", function (message) {
    var t = document.getElementById('task');
    t.innerHTML = `
        <tr id="task">
            <td>/nyokkey/hmi/task</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});
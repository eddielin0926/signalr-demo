// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.
startTime = new Date();

setInterval(() => {
    endTime = new Date();
    var timeDiff = new Date(endTime - startTime).toISOString().substring(11, 19);
    var t = document.getElementById("elapsed-time");
    t.innerHTML = `
        Elapsed Time: ${timeDiff}
    `
}, 1000);

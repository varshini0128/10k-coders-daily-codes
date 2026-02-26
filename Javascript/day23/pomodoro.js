var totalSeconds = 25 * 60;
var interval;

function showTime() {
    var minutes = Math.floor(totalSeconds / 60);
    var seconds = totalSeconds % 60;

    if (seconds < 10) {
        seconds = "0" + seconds;
    }

    document.getElementById("time").innerHTML = minutes + ":" + seconds;
}
let is_running=false
function start() {
    is_running=true
    interval = setInterval(function() {
        totalSeconds = totalSeconds - 1;
        showTime();

        if (totalSeconds < 0) {
            clearInterval(interval);
            alert("Time is over");
        }
    }, 1000);
}

function pause() {
    clearInterval(interval);
    is_running=false
}

function reset() {
    clearInterval(interval);
    totalSeconds = 25 * 60;
    is_running=false
    showTime();
}

showTime();

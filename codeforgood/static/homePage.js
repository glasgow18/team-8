function shiftOn() {
    document.getElementById("start").style.background='#FFD700';
}

function shiftOut() {
    document.getElementById("start").style.background='#FFA500';
}

function changeOn() {
    document.getElementById("escapeButton").style.background='#FFD700';
}

function changeOut() {
    document.getElementById("escapeButton").style.background='#FFFF00';
}

function closewindow()
{
alert("attempt window close!");
window.close();
}

function addmessage()
{
  print(document.getElementById("message").value);
}
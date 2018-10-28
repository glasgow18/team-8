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


function sendMessage() {
	const value = DOM.input.value;
	if (value === '') {
		return;
	}
	DOM.input.value = '';
	drone
}



function closewindow()
{
window.close()
}



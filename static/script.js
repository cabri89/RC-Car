var countKeyPress = 0;
document.addEventListener("DOMContentLoaded", function() {
  document.addEventListener("keydown", checkKeyPressed);
  document.addEventListener("keyup", stopMovement);
});

function sendMove(direction){
  // Set up our HTTP request
  var xhr = new XMLHttpRequest();

  // Setup our listener to process completed requests
  xhr.onload = function () {
    // Process our return data
    if (xhr.status >= 200 && xhr.status < 300) {
      // What do when the request is successful
    } else {
      // What do when the request fails
    }
    // Code that should run regardless of the request status
  };

  xhr.open('GET', 'move/' + direction);
  xhr.send();
}

function stopMovement(){
  countKeyPress = 0;
  // Set up our HTTP request
  var xhr = new XMLHttpRequest();

  // Setup our listener to process completed requests
  xhr.onload = function () {
    // Process our return data
    if (xhr.status >= 200 && xhr.status < 300) {
      // What do when the request is successful
    } else {
      // What do when the request fails
    }
    // Code that should run regardless of the request status
  };

  xhr.open('GET', 'stop/');
  xhr.send();
}


function checkKeyPressed(e) {
  if (countKeyPress == 1) {
    return;
  }else {
    countKeyPress++;
  }

  // z = 90 / s = 83 / q = 81 / d = 68
  //haut = 38 / bas = 40 / gauche = 37 / droite = 39
	if (e.keyCode === 90 || e.keyCode === 38) {
    sendMove(0);
	}else if (e.keyCode === 83 || e.keyCode === 40) {
    sendMove(1);
  }else if (e.keyCode === 81 || e.keyCode === 37) {
    sendMove(2);
  }else if (e.keyCode === 68 || e.keyCode === 39) {
    sendMove(3);
  }
}

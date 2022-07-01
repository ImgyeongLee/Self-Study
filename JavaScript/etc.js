var velocity = 1
var id = null

const button = document.getElementById('special-button')

function showProfile() {
  var profile = document.getElementById("profile");
  var pos = -800;
  clearInterval(id);
  id = setInterval(frame, 10);
  function frame() {
    if (pos >= -5) {
      velocity = 1
      clearInterval(id);
    } else {
      pos += velocity
      velocity += 0.5;
      profile.style.left = pos + 'px';
    }
  }
}

function hideProfile() {
  var profile = document.getElementById("profile");
  var pos = 0;
  clearInterval(id);
  id = setInterval(frame, 10);
  function frame() {
    if (pos <= -800) {
      velocity = 1
      clearInterval(id);
    } else {
      pos -= velocity
      velocity += 0.5;
      profile.style.left = pos + 'px';
    }
  }
}

function specialFunc(code) {
  if (code === "mirror") {
    button.style.display = 'block';
    button.innerText = "거울을 자세히 본다."
  }
  else if (code === "bookshelf") {
    button.style.display = 'block';
    button.innerText = "책을 하나 꺼낸다."
  }
  else if (code === "desk") {
    button.style.display = 'block';
    button.innerText = "컴퓨터를 본다."
  }
  else if (code === "bed") {
    button.style.display = 'block';
    button.innerText = "잠을 잔다."
  }
  else {
    button.style.display = 'none';
  }
}

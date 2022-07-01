const canvas = document.getElementById('main')
const ctx = canvas.getContext('2d')

const dialog = document.getElementById('dialog')
const diactx = dialog.getContext('2d')

const portrait = document.getElementById('portrait')
const porctx = portrait.getContext('2d')

canvas.width = 800
canvas.height = 400
dialog.width = 650
dialog.height = 128
portrait.width = 128
portrait.height = 128

const gravity = 0.15

class Player {
  constructor() {
    this.velocity = {
      x: 0,
      y: 1
    }
    this.width = 64
    this.height = 128
    this.position = {
      x: 150,
      y: 400 - this.height
    }
  }

  draw() {
    var img = new Image()
    img.src = "./img/character/sairan_child.png"
    ctx.drawImage(img,this.position.x, this.position.y, this.width, this.height)
  }

  update() {
    this.draw()
    this.position.x += this.velocity.x
    this.position.y += this.velocity.y

    if (this.position.y + this.height + this.velocity.y <= canvas.height) {
      this.velocity.y += gravity
    }
    else {
      this.velocity.y = 0
      flags.is_above.bit = false
    }

    if (this.position.x + this.width >= canvas.width)
      keys.right.pressed = false
    else if (this.position.x === 0)
      keys.left.pressed = false
  }

}

// The function for creating an object
class Object {
  constructor(code, xpos, ypos, width, height) {
    this.position = {
      x: xpos,
      y: ypos - height
    }
    this.ID = code
    this.width = width
    this.height = height
    this.description = ""
  }

  setDescription(desc) {
    this.description = desc
  }

// The function for letting the user know that they can interact with this object
  interactAlert(width) {
    ctx.fillStyle = 'yellow'
    ctx.fillRect(this.position.x + this.width / 2 - width / 2, this.position.y - this.height / 2 - 10, width, 32)

    if (keys.interact.pressed)
    {
      diactx.clearRect(0, 0, canvas.width, canvas.height)
      ctx.fillStyle = 'red'
      ctx.fillRect(this.position.x + this.width / 2 - width / 2, this.position.y - this.height / 2 - 10, width, 32)
      diactx.font = "20px sans-serif"
      diactx.fillText(this.description, 20, 64)
      specialFunc(this.ID)
    }
  }

  draw() {
    ctx.fillStyle = 'blue'
    ctx.fillRect(this.position.x, this.position.y, this.width, this.height)
  }

  update(player) {
    this.draw()
    if (player.position.x - player.width / 2 >= this.position.x - player.width / 2 && player.position.x - player.width / 2 <= this.position.x + this.width / 2) {
      this.interactAlert(32)
    }
  }
}


// Draw Player
const player = new Player()

// Draw Object
const mirror = new Object("mirror", 200, 380, 48, 84)
const desk = new Object("desk", 492, 400, 128, 84)
const closet = new Object("none", 300, 400, 84, 128)
const bookshelf = new Object("bookshelf", 384, 400, 108, 128)
const door = new Object("none", 100, 400, 64, 84)
const bed = new Object("bed", 620, 400, 180, 64)

// Set descriptions
mirror.setDescription("벽에 걸려있는 거울이다. 내 모습이 보인다.")
desk.setDescription("책상이다. 읽고 있던 책과 컴퓨터가 있다.")
closet.setDescription("내 옷장이다. 교복과 일상복 몇 벌 외에는 별 거 없다.")
door.setDescription("복도로 나가는 문이다. 지금은 썩 나가고픈 마음이 없다.")
bed.setDescription("폭신폭신한 침대다.")
bookshelf.setDescription("책장이다. 교과서들도 있고, 도서관에서 빌린 책들도 많다.")

const flags = {
  is_pause: {
    bit: false
  },
  is_above: {
    bit: false
  }
}

const keys = {
  right: {
    pressed: false
  },
  left: {
    pressed: false
  },
  interact: {
    pressed: false
  }
}

function animate() {
  requestAnimationFrame(animate)
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  mirror.update(player)
  desk.update(player)
  door.update(player)
  closet.update(player)
  bookshelf.update(player)
  bed.update(player)
  player.update()

  if (keys.right.pressed) {
    player.velocity.x = 2
  }
  else if (keys.left.pressed) {
    player.velocity.x = -2
  }
  else player.velocity.x = 0
}

animate()

window.addEventListener('keydown', ({ keyCode }) => {
  switch (keyCode) {
    case 65:
      console.log("Left")
      keys.left.pressed = true
      break

    case 68:
      console.log("Right")
      keys.right.pressed = true
      break

    case 32:
      console.log("Jump")
      if (flags.is_above.bit === false) {
        flags.is_above.bit = true
        player.velocity.y -= 5
      }
      break

    case 69:
      console.log("Interact")
      keys.interact.pressed = true
      break
  }
})

window.addEventListener('keyup', ({ keyCode }) => {
  switch (keyCode) {
    case 65:
      console.log("Left")
      keys.left.pressed = false
      break

    case 68:
      console.log("Right")
      keys.right.pressed = false
      break

    case 32:
      console.log("Jump")
      player.velocity.y = 0
      break

    case 69:
      console.log("Interact")
      keys.interact.pressed = false
      break
  }
})

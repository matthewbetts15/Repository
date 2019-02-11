import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop

def setup():
    print "Built with Processing Python version " + platform.python_version()

    global player, sprites
    size(515, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width / 2, height / 2, playerTeam)

    sprites.append(player)
    sprites.append(Enemy(50, 50, enemyTeam))
    sprites.append(Enemy(150, 150, enemyTeam))
    sprites.append(Raindrop(10, 0, enemyTeam))
    sprites.append(Raindrop(50, 0, enemyTeam))
    sprites.append(Raindrop(90, 0, enemyTeam))
    sprites.append(Raindrop(130, 0, enemyTeam))
    sprites.append(Raindrop(170, 0, enemyTeam))
    sprites.append(Raindrop(210, 0, enemyTeam))
    sprites.append(Raindrop(300, 0, enemyTeam))
    sprites.append(Raindrop(340, 0, enemyTeam))
    sprites.append(Raindrop(380, 0, enemyTeam))
    sprites.append(Raindrop(420, 0, enemyTeam))
    sprites.append(Raindrop(460, 0, enemyTeam))
    sprites.append(Raindrop(500, 0, enemyTeam))
    
def draw():
    global player, sprites
    background(255)

    for sprite in sprites:
        sprite.animate()

    checkCollisions()

def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2)) ** (0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)

def keyPressed():
    global player
    player.keyDown()

def keyReleased():
    global player
    player.keyUp()

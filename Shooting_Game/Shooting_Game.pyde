import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Sprite import Sprite
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    global player, sprites
    size(515, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width / 2, height/ 2, playerTeam)

    SpriteManager.spawn(player)
    SpriteManager.spawn(Enemy(50, 50, enemyTeam))
    SpriteManager.spawn(Enemy(150, 150, enemyTeam))
    SpriteManager.spawn(Raindrop(10, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(50, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(90, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(130, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(170, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(210, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(300, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(340, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(380, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(420, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(460, 0, enemyTeam))
    SpriteManager.spawn(Raindrop(500, 0, enemyTeam))
    SpriteManager.spawn(JiggleBot(random(0,515), random(0,250), enemyTeam))
    SpriteManager.spawn(JiggleBot(random(0,515), random(0,250), enemyTeam))
    SpriteManager.spawn(ScreenSaverBot(random(0,500), 0, enemyTeam))
    SpriteManager.spawn(ScreenSaverBot(random(0,500), 0, enemyTeam))
    SpriteManager.spawn(ScreenSaverBot(random(0,500), 0, enemyTeam))
    SpriteManager.spawn(ScreenSaverBot(random(0,250), 0, enemyTeam))
    SpriteManager.spawn(ScreenSaverBot(random(0,250), 0, enemyTeam))
    
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

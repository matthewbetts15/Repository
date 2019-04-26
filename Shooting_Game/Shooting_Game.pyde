import platform
import SpriteManager

from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Sprite import Sprite





def setup():
    print "Built with Processing Python version " + platform.python_version()
    global player, sprites
    size(700, 700)
    playerTeam = 1
    enemyTeam = 2
    powerTeam = 3
    player = Player(width / 2, height/ 2, playerTeam)

    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Enemy(50, 50, enemyTeam))
    
def draw():
    background(255)    
    SpriteManager.animate()

def keyPressed():
    SpriteManager.player.keyDown()

def keyReleased():
    SpriteManager.player.keyUp()

import SpriteManager
class Armour:

    armour = 10
    
    def display(self):
        stroke(100)
        strokeWeight(self.armour)
        fill(255, 0, 0)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
                
    def handleCollision(self):
        self.armour -= 1
        if self.armour < 1:
            SpriteManager.destroy(self)
        

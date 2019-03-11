from Bullet import Bullet

import math
import SpriteManager

class Shooter:
    mark = 0
    wait = 1000

    def move(self):
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
            
        
    def aim (self, target):
        p1 = target.x - self.x
        p2 = target.y - self.y
        d = math.sqrt(p1**2 + p2**2)
        xUnit = p1/d * 5
        yUnit = p2/d * 5
        return PVector(xUnit, yUnit)
    
    def fire(self, vector):
        if(millis() - self.mark > self.wait):
            self.mark = millis()
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))

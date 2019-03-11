from Sprite import Sprite


class JiggleBot(Sprite):
    
    speed = 4
    diameter = 30
    c = color(90,2,2)
        
    def move(self):
       self.y += random(-self.speed, self.speed)
       self.x += random(-self.speed, self.speed)
       self.x = constrain(self.x, 0, width)
       self.y = constrain(self.y, 0, height)
       

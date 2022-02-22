# The "Food" class
import random
class Food():

    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 1.0
        self.maxforce = 0.01
        self.count = 0

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)
        
    def getPosition(self):
        return self.position
    
    def setPosition(self):
        foodX = random.randrange(4, 639)
        foodY = random.randrange(15, 359)
        position = PVector(foodX, foodY)
        self.position = position
        self.count = self.count+1
    def getCount(self):
        return self.count
    
    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading()
        fill(35, 46, 209)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            rect(0, 0, self.r, self.r)
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)

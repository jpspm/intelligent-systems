# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

import random
from Vehicle import Vehicle
from Food import Food
def setup():
    global vehicle
    global foodX
    global foodY
    global food
    global update
    global count
    size(640, 360)
    velocity = PVector(0, 0)
    velocity1 = PVector(0,0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    foodX = random.randrange(1, 640)
    foodY = random.randrange(1, 360)
    food = Food(foodX, foodY, velocity1)
    count = int(0)
    
def draw():
    background(253)
    velocity = PVector(0, 0)
    food.update()
    food.display()
    vehicle.update()
    vehicle.display()
    velocity = vehicle.getPosition()
    velocity2 = food.getPosition()
    if ((food.getPosition().dist(vehicle.getPosition()) > 0.5)):
        vehicle.applyForce(velocity2 - velocity)
    else:
        velocity = PVector(0, 0)
        vehicle.setVelocity(velocity)
        food.setPosition()
        print("agente guloso ja comeu "+str(food.getCount())+" comidoncios")
        
    vehicle.update()
    vehicle.display()

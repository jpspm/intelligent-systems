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
    global f
    size(640, 360)
    velocity = PVector(0, 0)
    velocity1 = PVector(0,0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    foodX = random.randrange(1, 640)
    foodY = random.randrange(1, 360)
    food = Food(foodX, foodY, velocity1)
    #count = int(0)
    f = createFont("Roboto",16,True)
    
def draw():
    background(13, 19, 23)
    velocity = PVector(0, 0)
    textFont(f, 16)
    text("Agente guloso ja comeu "+str(food.getCount())+" comidoncios", 3, 15)
    fill(31, 36, 33)
    food.update()
    food.display()
    vehicle.update()
    vehicle.display()
    velocity = vehicle.getPosition()
    velocity2 = food.getPosition()
    if ((food.getPosition().dist(vehicle.getPosition()) > 3)):
        vehicle.applyForce(velocity2 - velocity)
        speed = (float)(food.getPosition().dist(vehicle.getPosition()))
        vehicle.setMaxspeed(speed)
    else:
        velocity = PVector(0, 0)
        vehicle.setVelocity(velocity)
        food.setPosition()
        
    vehicle.update()
    vehicle.display()

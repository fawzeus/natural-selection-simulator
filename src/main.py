import pygame
import sys
import time
from CONSTANTS import*
from Creature import Creature
from Food import Food
import math

def distance(pos1,pos2):
    x1,y1=pos1
    x2,y2=pos2
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
def check_for_eat(creatures,foods):
    for creature in creatures:
        for food in foods:
            if distance(creature.position,food.position) <=FOOD_SIZE+CREATURE_SIZE:
                food.isEaten=True
                creature.energy+=1000

def draw_Items(screen,creatures)->None:
    for creature in creatures:
        pygame.draw.circle(screen, creature.color, creature.position, creature.size)
def move (creatures)->None:
    for creature in creatures:
        creature.move()

def Check(food,creatures):
    index=0
    while index<len(creatures):
        if not creatures[index].isAlive:
            del creatures[index]
        else:
            index+=1
    index=0
    while index<len(food):
        if food[index].isEaten:
            del food[index]
        else:
            index+=1
# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Natural Selection Simulator")
creatures=[]
for i in range(NUMBER_OF_CREATURES):
    creatures.append(Creature())
food=[]
for i in range(NUMBER_OF_FOOD):
    food.append(Food())
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update game state

    # Draw to the screen
    screen.fill((255, 255, 255))  # Fill the screen with white
    Check(food,creatures)
    draw_Items(screen,creatures)
    draw_Items(screen,food)
    move(creatures)
    check_for_eat(creatures,food)
    time.sleep(0.01)


    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()


import math
from Food import Food
from CONSTANTS import *
import pygame
def distance(pos1,pos2):
    x1,y1=pos1
    x2,y2=pos2
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
def check_for_eat(creatures,foods):
    for creature in creatures:
        for food in foods:
            if distance(creature.position,food.position) <=FOOD_SIZE+creature.size:
                food.isEaten=True
                creature.foodEaten+=1
def check_for_multiply(creatures):
    for creature in creatures:
        if creature.foodEaten>=2:
            print("miltiply")
            creatures.append(creature.multiply())
def check_for_death_and_multiply(creatures):
    newCreatures=[]
    for creature in creatures:
        if creature.foodEaten>=2:
            newCreatures.append(creature.multiply())
            creature.foodEaten=0
        elif creature.foodEaten==1:
            creature.foodEaten=0
        else:
            creature.isAlive=False
    creatures.extend(newCreatures)

def draw_Items(screen,creatures)->None:
    for creature in creatures:
        pygame.draw.circle(screen, creature.color, creature.position, creature.size)
def move (creatures)->None:
    for creature in creatures:
        creature.move()

def avg_speed(creatures):
    avg=0
    if len(creatures)==0:
        return 0
    for creature in creatures:
        avg+=creature.speed
    return avg/len(creatures)
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
def generate_food(food,amount=NUMBER_OF_FOOD):
    if amount<=0:
        return
    for _ in range(amount):
        food.append(Food())

def Creatures_Scan(creatures,foods):
    for creature in creatures:
        creature.scan(foods)
    
def restart(creatures,foods):
    for creature in creatures:
        creature.check_for_target_existance(foods)
import pygame
import sys
import time
from CONSTANTS import*
from Creature import Creature
from Food import Food
import math
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from utils import *

matplotlib.use('TkAgg')  # or 'Qt5Agg' depending on your environment
# Initialize Pygame
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 36)  # You can choose the font and size

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Natural Selection Simulator")
creatures=[]
for i in range(NUMBER_OF_CREATURES):
    creatures.append(Creature())
food=[]
generate_food(food)
# Game loop

step=0
amount=50
generation=1
avg_speed_axis=[]
number_of_creatures_axis=[]
x_axis=[]

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True, figsize=(8, 6))
ax1.set_ylabel('Avg Speed', color='blue')
ax2.set_ylabel('Number of Creatures', color='orange')
ax2.set_xlabel('Generation')

# Set initial y-axis limits for better visualization
ax1.set_ylim(1, 1.5)  # Adjust the values based on your data characteristics for avg speed
ax2.set_ylim(0, 100)  # Adjust the values based on your data characteristics for number of creatures

line_speed, = ax1.plot([], [], label='Avg Speed', linewidth=2.0, color='blue')
line_creatures, = ax2.plot([], [], label='Number of Creatures', color='orange', linewidth=2.0)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

while True:
    #amount=50
    step+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update game state

    # Draw to the screen
    Creatures_Scan(creatures,food)
    screen.fill((255, 255, 255))  # Fill the screen with white
    draw_Items(screen,creatures)
    draw_Items(screen,food)
    move(creatures)
    check_for_eat(creatures,food)
    Check(food,creatures)
    restart(creatures,food)
    if step==4000 or len(food)==0:
        check_for_death_and_multiply(creatures)
        generate_food(food,amount)
        print(len(food))
        step=0
        #amount-=1
        generation+=1
        x_axis.append(generation)
        y_axis_speed = avg_speed(creatures)
        avg_speed_axis.append(y_axis_speed)
        line_speed.set_data(x_axis, avg_speed_axis)
        number_of_creatures_axis.append(len(creatures))
        line_creatures.set_data(x_axis, number_of_creatures_axis)
        if min(avg_speed_axis) != max (avg_speed_axis):
            ax1.set_ylim(min(avg_speed_axis), max(avg_speed_axis)) 
        else:
            ax1.set_ylim(0,2) 
        if min(number_of_creatures_axis) != max(number_of_creatures_axis):
            ax2.set_ylim(min(number_of_creatures_axis),max(number_of_creatures_axis))
        else:
            ax2.set_ylim(0, 100) 
        ax1.relim()
        ax1.autoscale_view()

        ax2.relim()
        ax2.autoscale_view()

        plt.pause(0.01)  # Pause to allow for dynamic updating


    # Update display
    text= f"food : {len(food)}"
    text_render = font.render(text, True, (0, 0, 0))  
    text2=f"Creatures : {len(creatures)}"
    text_render2=font.render(text2, True, (0, 0, 0))  
    screen.blit(text_render, (15,15))
    screen.blit(text_render2,(15,50))
    
    time.sleep(0.01)
    pygame.display.flip()

# Quit Pygame
pygame.quit()

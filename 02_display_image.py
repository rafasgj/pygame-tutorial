#!/usr/bin/env python3

import pygame

from collections import namedtuple
from colors import black, white

display_config = namedtuple('DisplayConfig','width height')(800,600)

def ignore_event(event):
    print("Event Name: {}".format(pygame.event.event_name(event.type)))


def end_running(event):
    global running
    print("End running.")
    running = False

# initializes pygame
pygame.init()

# start display
win = pygame.display.set_mode((800,600))
pygame.display.set_caption('Racing Wheels')

# create a time to track game time
clock = pygame.time.Clock()

# load images
car_image = pygame.image.load("images/racecar.png")
car_position = ((display_config.width * 0.45), (display_config.height * 0.8))

def display_car():
    win.blit(car_image, car_position)

# define an event dictionary
events = {
    pygame.QUIT: end_running
}

# main loop
running = True
while running:
    # process event queue
    for event in pygame.event.get():
        fn = events.get(event.type, ignore_event)
        fn(event)

    # clear background
    win.fill(white)
    
    # draw objects
    display_car()    

    # update display
    pygame.display.update()
    # update clock
    clock.tick(60)

# end pygame program
pygame.quit()


#!/usr/bin/env python3

import pygame

from collections import namedtuple
from colors import black, white

display_config = namedtuple('DisplayConfig','width height')(800,600)

def move_left(event):
    global xchange
    xchange = -5

def move_right(event):
    global xchange
    xchange = +5

def pass_fn(*args, **kwargs):
    pass

def end_running(event):
    global running
    print("End running.")
    running = False

def keyboard_down(event):
    key_events = {
        pygame.K_ESCAPE: end_running,
        pygame.K_LEFT: move_left,
        pygame.K_RIGHT: move_right,
    }

    kfn = key_events.get(event.key, pass_fn)
    kfn(event)

def keyboard_up(event):
    # stop move
    global xchange
    xchange = 0

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
xchange = 0

def display_car():
    win.blit(car_image, car_position)

# define an event dictionary
events = {
    pygame.QUIT: end_running,
    pygame.KEYDOWN: keyboard_down,
    pygame.KEYUP: keyboard_up,
}

# main loop
running = True
while running:
    # process event queue
    for event in pygame.event.get():
        fn = events.get(event.type, pass_fn)
        fn(event)

    # update data model
    car_x, car_y = car_position
    car_position = (car_x + xchange, car_y)

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


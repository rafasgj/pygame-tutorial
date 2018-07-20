#!/usr/bin/env python3

import pygame

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

    # update display
    pygame.display.update()
    # update clock
    clock.tick(60)

# end pygame program
pygame.quit()

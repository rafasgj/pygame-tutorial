#!/usr/bin/env python3

import pygame

from collections import namedtuple
from colors import black, white

from time import sleep

# initializes pygame
pygame.init()

# initialize display
display_config = namedtuple('DisplayConfig','width height')(800,600)

win = pygame.display.set_mode(display_config)
pygame.display.set_caption('Racing Wheels')

# create a time to track game time
clock = pygame.time.Clock()


class GameObject(object):
    def __init__(self, imagefile, position):
        self.image = pygame.image.load(imagefile)
        self.position = position

    @property
    def width(self):
        return self.image.get_width()

    @property
    def height(self):
        return self.image.get_height()

    def move(self, delta):
        x, y = self.position
        dx, dy = delta
        self.position = (x + dx, y + dy)
 
    def render(self, display):
        display.blit(self.image, self.position)

    def hit(self, bullet):
        x, y = self.position
        w, h = self.image.get_size()
        bx, by, bw, bh = bullet
        if x + w < bx or x > bx + bw:
            return false
        if y + h < by or y > by + bh:
            return false
        return true


    def hit_bounds(self):
        x, y = self.position
        w, h = self.image.get_size()
        if x < 0 or x + w > display_config.width:
            return True
        if y < 0 and y + h > display_config.height:
            return True
        return False


def move_left(event):
    global xchange
    xchange = -5


def move_right(event):
    global xchange
    xchange = +5


def pass_fn(*args, **kwargs):
    pass


running = True
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


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, size=80):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ([i/2 for i in display_config])
    win.blit(TextSurf, TextRect)


def game_over(*args, **kwargs):
    win.fill(white)
    message_display("Game Over", 115)
    pygame.display.update()
    sleep(2)
    pygame.quit()
    quit()

xchange = 0
def game_loop(model_update, render_objects, events, fps=60):
    global running
    running = True
    while running:
        # process event queue
        for event in pygame.event.get():
            fn = events.get(event.type, pass_fn)
            fn(event)

        model_update()

        win.fill(white)

        render_objects(win)        

        pygame.display.update()
        clock.tick(fps)


# Introduction layout
intro_events = {
    pygame.QUIT: game_over,
    pygame.KEYDOWN: end_running,
}


def intro_render(display):
    message_display("Press a Key to Start!")


# game layout
# define an event dictionary
game_events = {
    pygame.QUIT: end_running,
    pygame.KEYDOWN: keyboard_down,
    pygame.KEYUP: keyboard_up,
}

# game objects
car = GameObject('images/racecar.png', [i/2 for i in display_config])


def game_model_update():
    car.move((xchange, 0))
    if car.hit_bounds():
        game_over()


def game_render(display):
    car.render(display)


# initial game screen
game_loop(pass_fn, intro_render, intro_events)
# main game loop
game_loop(game_model_update, game_render, game_events)
# end pygame program
pygame.quit()
quit()


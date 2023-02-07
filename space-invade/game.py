import pygame
import time
import random
import os

pygame.init()


size = width, height = 1200, 831
screen = pygame.display.set_mode(size)
bg = pygame.image.load("spase.gif") 

def game():

    
        #draw screen, music begin
    
            

        #set score to 0
        #splash screen, "insert coin/press any button" prompt
        #screen switches when button pressed
        #spawn barriers
        #2 barriers, one on each side of the screen
        #barriers block all bullets
        #barriers never disappear
        #player spawn
        #set player hp
            
        #player control functions
    pygame.key.set_repeat(0, 1)
    keys = pygame.key.get_pressed()
        #left arrow/A pressed, move left
    if keys[pygame.K_LEFT]:
        pass
        #right arrow/D pressed, move right
    if keys[pygame.K_RIGHT]:
        pass
        #space pressed, shoot
        #if player hp hits 0
            #show explosion
            #wait 1 second
            #go to game start screen

run = True

while run:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

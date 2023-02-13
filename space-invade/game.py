import pygame
import time
import random
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

pygame.init()
screen = pygame.display.set_mode([1200, 831])
bg = pygame.image.load("spase.gif") 
font = pygame.font.SysFont
font1 = font("arial", 24)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)

player = Sprite("ship.gif")

def show_time():
    screen.blit(player.image, (10, 10))

def init():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nExit from pygame\n\n")
            sys.exit()
    show_time()
    clock.tick(60)
    pygame.display.update()



def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pygame.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

0


        
def update(self):
    pos = pygame.mouse.get_pos()
    self.rect.topleft = pos
    self.rect.move_ip(self.ship_offset)
        


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
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






        #if player hp hits 0

                #show explosion

                #wait 1 second

                #go to game start screen
    screen.blit(bg, (0, 0))
    pygame.display.flip()


import pygame
import time
import sys
pygame.init()

screen = pygame.display.set_mode((500,500))

while True:
    new_event = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
        elif event.type == pygame.KEYUP:
            print('NO!')
    #time.sleep(1)
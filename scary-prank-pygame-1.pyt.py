import pygame
from time import sleep

pygame.init()

window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

#for loading audio------>
pygame.mixer.init()
pygame.mixer.music.load("ratsasan.mp3")
pygame.mixer.music.play()
sleep(10)
#final sound-------------
pygame.mixer.music.load("scary.mp3")
pygame.mixer.music.play()
sleep(2)

#bring the scary image-------------
scary_image = pygame.image.load("scr.jpg")
#show the image-------------
#blit-->block image transfer
window.blit(scary_image,(0,0))
pygame.display.update()
sleep(3)
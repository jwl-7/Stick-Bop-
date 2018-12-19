import pygame
import random
import os

# look in dir that python file is in
os.chdir(os.path.dirname(__file__))

SCREEN_WIDTH  = 900
SCREEN_HEIGHT = 700

# monokai color palette
white  = (253, 250, 243)
brown  = ( 45,  43,  46)
pink   = (255,  96, 137)
green  = (169, 220, 199)
yellow = (255, 216, 102)
orange = (252, 151, 105)
purple = (171, 157, 244)
blue   = (119, 220, 230)

score = 0

def main():
    pygame.init()
    size   = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()
    pygame.display.set_caption('Stick Bop! < TEST >')

    # display background image
    background_image = pygame.image.load('stick_pic.png').convert()
    screen.blit(background_image, [0, 0])

    # play background music
    #pygame.mixer.music.load('background_arcade_music.mp3')
    #pygame.mixer.music.set_volume(0.08)
    #pygame.mixer.music.play(-1)

    # loop until user presses close button
    done = False

    # program loop
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # change image when key(left arrow) is pressed -- image stays after keypress
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:

                    pygame.mixer.music.load('sword_ahhhh.wav')
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(0)

                    image2 = pygame.image.load('stick_pic_sword.png').convert()
                    screen.blit(image2, [0, 0])

            # change image when key(left arrow) is released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    background_image = pygame.image.load('stick_pic.png').convert()
                    screen.blit(background_image, [0, 0])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
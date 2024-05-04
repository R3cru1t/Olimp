import pygame
import random
import time
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
x1, x2, x3 = 0, 0, 0
stop = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.rect(screen, "gray", pygame.Rect(0, 60, 1280, 100))
    pygame.draw.rect(screen, "gray", pygame.Rect(0, 300, 1280, 100))
    pygame.draw.rect(screen, "gray", pygame.Rect(0, 540, 1280, 100))

    car1 = pygame.image.load("images/car1.png")
    car2 = pygame.image.load("images/car2.png")
    car3 = pygame.image.load("images/car3.png")


    def cars(x1, x2, x3):

        screen.blit(car1, (x1, -20))
        screen.blit(car2, (x2, 260))
        screen.blit(car3, (x3, 530))

    x1_speed = random.randint(1, 10)
    x2_speed = random.randint(1, 10)
    x3_speed = random.randint(1, 10)

    x1 = x1 + x1_speed
    x2 = x2 + x2_speed
    x3 = x3 + x3_speed
    cars(x1, x2, x3)
    time.sleep(0.001)


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen

    clock.tick(60)  # limits FPS to 60
    if x1 >= 1000 or x2 >= 1000 or x3 >= 1000:
        font = pygame.font.SysFont(None, 24)
        if x1 >= 1000:
            text = font.render('Red car won', True, (0, 0, 0))
            screen.blit(text, (20, 20))
            if stop == False:
                pygame.display.update()
            stop = True

        if x2 >= 1000:
            text = font.render('White car won', True, (0, 0 ,0))
            screen.blit(text, (20, 20))
            if stop == False:
                pygame.display.update()
            stop = True


        if x3 >= 1000:
            text = font.render('Black car won', True, (0, 0 ,0))
            screen.blit(text, (20, 20))
            if stop == False:
                pygame.display.update()
            stop = True

    if stop == False:
        pygame.display.update()


            

pygame.quit()
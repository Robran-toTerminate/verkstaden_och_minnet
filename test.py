import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000,400), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
running = True

color = 'purple'

img = pygame.image.load("/Users/home/Desktop/devstuff/code/verkstaden_och_minnet/image.png")
imgX = 10
imgY = 10
imgXV = 10
imgYV = 10
imgW = img.width

scale_factor = -5

imgH = 160


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == 32:
            color = 'green'

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > imgX and event.pos[0] < imgX + imgW:
                if event.pos[1] > imgY and event.pos[1] < imgY + imgH:
                    color = 'blue'


    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color)

    if imgX+imgW > screen.width or imgX < 0:
        imgXV *= -1
    if imgY+imgH > screen.height or imgY < 0:
        imgYV *= -1

    imgX += imgXV
    imgY += imgYV
    imgW += scale_factor

    if imgW < 20:
        img = pygame.transform.flip(img, True, False)
        scale_factor *= -1
    elif imgW > screen.width-200:
        scale_factor *= -1
    else:
        screen.blit(pygame.transform.scale(img, (imgW, imgH)), (imgX,imgY))



    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
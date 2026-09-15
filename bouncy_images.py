import pygame

#Funkar inte riktigt men orkar egentligen inte fixas

class square(): 
    posx = 0
    posy = 0
    vx = 1
    vy = 1
    img = pygame.transform.scale(pygame.image.load("/Users/home/Desktop/devstuff/code/verkstaden_och_minnet/image.png"),(100,100))
    
    
square_speed = 10

pygame.init()
screen = pygame.display.set_mode((1000,600), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
running = True

active_squares = [square()]

new_square = square()
new_square.posy = 200
new_square.posx = 600
active_squares.append(new_square)

new_square2 = square()
new_square2.posy = 200
new_square2.posx = 400
active_squares.append(new_square2)

while running:
    screen.fill('green')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for s in active_squares:
        s.posx += s.vx * square_speed
        s.posy += s.vy * square_speed

        if s.posx + s.img.width > screen.width or s.posx < 0:
            s.vx *= -1
        if s.posy + s.img.height > screen.height or s.posy < 0:
            s.vy *= -1  

        for ss in active_squares:
            if s == ss:
                continue
            if s.posx + s.img.width > ss.posx and s.posx < ss.posx + ss.img.width and s.posy + s.img.height > ss.posy and s.posy < ss.posy + ss.img.height:
                
                if s.posx + s.img.width > ss.posx:
                    s.vx *= -1
                elif s.posx < ss.posx + ss.img.width:
                    s.vx *= -1
                if s.posy < ss.posy+ss.img.height:
                    s.vy *= -1
                elif s.posy +s.img.height > ss.posy:
                    s.vy *= -1
                print(s.posy+s.img.height)
                print(ss.posy)
                print(s.vy)
 

                print("Jobbhej")
            #if s.posy + s.img.height > ss.posy and s.posy < ss.posy - ss.img.height:
             #   s.vy *= -1  

        screen.blit(s.img,(s.posx,s.posy))

    pygame.display.flip()
    clock.tick(10)


pygame.quit()
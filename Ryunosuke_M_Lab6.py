import pygame, math
pygame.init()
screen = pygame.display.set_mode((800,600))
rect = pygame.Rect(300,250,200,100)
pygame.draw.rect(screen,(255,255,255),rect)

pygame.draw.circle(screen,(255,255,255), (350,375), 25)
pygame.draw.circle(screen,(255,255,255), (450,375), 25)

pygame.draw.arc(screen,(255,255,255), (350,225,100,50), 0, math.pi, 1)
pygame.display.update()

done=False
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
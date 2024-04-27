import pygame,sys
pygame.__init__()

DISPLAYSCREEN = pygame.display.set_mode((1200,800))
DISPLAYSCREEN.fill((0,0,255))
pygame.display.set_caption("BLUE SKY!")
FramePerSec = pygame.time.Clock()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygamme.quit()
      sys.exit()
    pygame.display.update()  
    FramePerSec.tick(60)

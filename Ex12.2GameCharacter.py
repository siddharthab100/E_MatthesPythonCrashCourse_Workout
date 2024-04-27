import sys, pygame
pygame.init()

DisplaySurf = pygame.display.set_mode((500,300))
DisplaySurf.fill((231,125,17))
pygame.display.set_caption("Game Character Entry!")
FramePerSec = pygame.time.Clock()

class GameChar:
    def __init__(self):
        self.screen = DisplaySurf
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("/home/siddhartha/Downloads/GameChar.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        self.screen.blit(self.image, self.rect)


G1 = GameChar()
while True:
  for event in pygame.event.get():
    if event == pygame.QUIT:
      pygame.quit()
      sys.exit()
    G1.draw()  
    pygame.display.flip()   
    FramePerSec(60)

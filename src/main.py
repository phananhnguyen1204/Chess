import pygame
import sys

from const import *

class Main:

  def __init__(self) -> None:
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Chess')

  def mainloop(self):
    while True:
      for event in pygame.event.get():
        if(event == pygame.QUIT):
          pygame.quit()
          sys.exist()
      pygame.display.update()

main = Main()
main.mainloop()
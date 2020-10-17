import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Game loop.
i = 0
while True:
  screen.fill((i, i, i))
  i = i + 1
  if (i >= 255):
      i = 0
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Update.

  # Draw.

  pygame.display.flip()
  fpsClock.tick(fps)

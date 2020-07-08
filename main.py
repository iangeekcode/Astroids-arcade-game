import pygame as py
from ship import *
from asteroid import *



py.init()
screen_info = py.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)



screen = py.display.set_mode(size)
clock = py.time.Clock()
color = (30, 0, 30)
screen.fill(color)



NumLevels = 4
CurrentLevels = 1
AstroidCount = 3
player = ship((20,300))
Asteroid = asteroid((300, 300))



def main():
  while True:
    clock.tick(60)
    for event in py.event.get():
      if event.type == py.KEYDOWN:
        if event.key == py.K_RIGHT:
          player.speed[0] = 5
        if event.key == py.K_LEFT:
          player.speed[0] = -5
        if event.key == py.K_UP:
          player.speed[1] = -5
        if event.key == py.K_DOWN:
          player.speed[1] = 5
      else:
        player.speed[0] = 0
        player.speed[1] = 0
    screen.fill(color)
    screen.blit(player.image, player.rect)
    player.update()
    py.display.flip()



if __name__=="__main__":
  main()
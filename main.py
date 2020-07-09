import pygame as py, random
from py. locals import *
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
CurrentLevels = 0
AsteroidCount = 0
player = ship((20,300))
Asteroids = py.sprite.Group()


def init():
  global AsteroidCount, CurrentLevels
  player.reset((20, 300))
  CurrentLevels += 1
  AsteroidCount += 3
  Asteroids.empty()
  player.reset
for i in range(AsteroidCount):
  Asteroids.add(asteroid((random.randint(0 , 800), random.randint(0, 600))))





def main():
  init()
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
    Asteroids.draw(screen)
    Asteroids.update()
    screen.blit(player.image, player.rect)
    player.update()
    py.display.flip()
    
    if player.checkReset == True(800):
      init()



if __name__=="__main__":
  main()


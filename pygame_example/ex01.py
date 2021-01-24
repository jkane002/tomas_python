import pygame
import os

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60,50
FPS = 60
WIDTH, HEIGHT = 1500, 900
vel = 5

BORDER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_SCALED = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_SCALED = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
red = pygame.Rect(1000, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game")

YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP_SCALED, 90)
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP_SCALED, 270)

def yellow_handle_movement(keys_pressed, yellow):
      if keys_pressed[pygame.K_a] and yellow.x - vel > 0:
          yellow.x -= vel
      # LEFT
      if keys_pressed[pygame.K_d] and yellow.x + SPACESHIP_WIDTH - 20 + vel < BORDER.x:
          yellow.x += vel
      # RIGHT
      if keys_pressed[pygame.K_w] and yellow.y - vel > 0:
          yellow.y -= vel
      # UP
      if keys_pressed[pygame.K_s] and yellow.y + SPACESHIP_HEIGHT + 5 + vel < HEIGHT:
          yellow.y += vel
      # DOWN

def red_handle_movement(keys_pressed, red):
      if keys_pressed[pygame.K_LEFT] and red.x - vel > BORDER.x:
          red.x -= vel
      # LEFT
      if keys_pressed[pygame.K_RIGHT] and red.x + vel + SPACESHIP_WIDTH - 10 < WIDTH:
          red.x += vel
      # RIGHT
      if keys_pressed[pygame.K_UP] and red.y - vel + 5 > 0:
          red.y -= vel
      # UP
      if keys_pressed[pygame.K_DOWN] and red.y + SPACESHIP_HEIGHT + 5 + vel < HEIGHT:
          red.y += vel
      # DOWN

def draw_window(red, yellow):
    WIN.fill((40, 20, 150))
    pygame.draw.rect(WIN, (0,0,0), BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)
    pygame.quit()

if __name__=="__main__":
    main()

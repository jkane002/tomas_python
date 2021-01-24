import pygame
import os

pygame.font.init()
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60,50
FPS = 60
WIDTH, HEIGHT = 1500, 900
vel = 5
BULLET_VEL = 7
BORDER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)
MAX_BULLETS = 5
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
pygame.mixer.init()
BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/grenade.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/gun.mp3')



YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_SCALED = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_SCALED = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))




WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game")

YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP_SCALED, 90)
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP_SCALED, 270)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, (255, 255, 255))
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /2, HEIGHT/2 - draw_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(5000)

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
      bullet.x += BULLET_VEL
      if red.colliderect(bullet):
          pygame.event.post(pygame.event.Event(RED_HIT))
          yellow_bullets.remove(bullet)
      elif bullet.x > WIDTH:
          yellow_bullets.remove(bullet)

    for bullet in red_bullets:
      bullet.x -= BULLET_VEL
      if yellow.colliderect(bullet):
          pygame.event.post(pygame.event.Event(YELLOW_HIT))
          red_bullets.remove(bullet)
      elif bullet.x < 0:
          red_bullets.remove(bullet)


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

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.fill((40, 20, 150))
    pygame.draw.rect(WIN, (0,0,0), BORDER)
    red_health_text = HEALTH_FONT.render( "Health: " + str(red_health), 1, (255,255,255))
    yellow_health_text = HEALTH_FONT.render( "Health: " + str(yellow_health), 1, (255,255,255))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255,0,0), bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255,255,0), bullet)

    pygame.display.update()

def main():
    red_health = 10
    yellow_health = 10
    yellow_bullets = []
    red_bullets = []
    red = pygame.Rect(1000, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
                # subtract 1 from yellow's health
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    pygame.quit()

if __name__=="__main__":
    main()

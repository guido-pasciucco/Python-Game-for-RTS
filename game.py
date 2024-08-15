import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game for Rocket Tech School - By Guido Pasciucco")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

bullet_width, bullet_height = 5, 10
bullet_speed = 10

enemy_width, enemy_height = 50, 50
enemy_speed = 5

bullets = []
enemies = []

score = 0
font = pygame.font.SysFont(None, 55)

running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_width:
        player_x += player_speed

    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_width // 2, player_y])

    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
    if random.randint(1, 20) == 1:
        enemies.append([random.randint(0, WIDTH - enemy_width), -enemy_height])
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
    for bullet in bullets:
        for enemy in enemies:
            if (enemy[0] < bullet[0] < enemy[0] + enemy_width and
                    enemy[1] < bullet[1] < enemy[1] + enemy_height):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))
    for enemy in enemies:
        pygame.draw.rect(screen, BLACK, (enemy[0], enemy[1], enemy_width, enemy_height))
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()
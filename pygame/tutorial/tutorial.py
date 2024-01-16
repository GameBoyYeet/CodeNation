# Based on https://https://www.youtube.com/watch?v=AY9MnQ4x3zk with modifications
from random import randint
import pygame
from sys import exit


def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = font.render(str(current_time), False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surf, obstacle_rect)
            else: screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]

        return obstacle_list
    else:
        return []


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Tutorial")
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 100)
game_active = False
start_time = 0
score = 0

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

gameover_surf = font.render('Game Over :(', False, 'White')
gameover_rect = gameover_surf.get_rect(center=(400, 200))

# Obstacles
snail_surf = pygame.image.load('graphics/snail/snail1.png')
snail_rect = snail_surf.get_rect(center=(800, 300))
fly_surf = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(200, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_title = font.render('Pygame Runner', False, 'Black')
game_title_rect = game_title.get_rect(center=(400, 50))
game_message = font.render('Press space to jump', False, 'Black')
game_message_rect = game_message.get_rect(center=(400, 330))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: player_gravity = -20
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1000), 300)))
                else:
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1000), 300)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player_rect = player_surf.get_rect(midbottom=(200, 300))
                snail_rect.left = 800
                game_active = True

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        start_time = pygame.time.get_ticks()
        screen.fill((94, 129, 162))
        screen.blit(game_title, game_title_rect)
        screen.blit(player_stand, player_stand_rect)

        score_message = font.render(f"Score: {score}", False, 'Black')
        score_message_rect = score_message.get_rect(center=(400, 330))

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)

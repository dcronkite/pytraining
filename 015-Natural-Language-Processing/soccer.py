import sys

import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 148, 189)
GREEN = (64, 173, 38)
GRAY = (117, 117, 117)
RED = (94, 28, 13)

# location
WIDTH = 800
HEIGHT = 500

# ball
SPEED_X = 3
SPEED_Y = -3
RADIUS = 20
BALL_START_X = WIDTH // 2
BALL_START_Y = HEIGHT // 2
BALL_X = BALL_START_X
BALL_Y = BALL_START_Y

# player
PLAYER_SPEED = 5

# player1
P1_X = 10
P1_Y = 10
P1_W = 25
P1_H = 100

# player2
P2_W = 25
P2_H = 100
P2_Y = 10
P2_X = WIDTH - P2_W - 10

# scores
SCORE1 = 0
SCORE2 = 0

# game speed
GAME_SPEED = 40
CLOCK = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Indoor Soccer')
pygame.mouse.set_visible(0)  # make mouse invisible
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # width/height

while True:
    screen.fill(WHITE)
    scoreboard = pygame.font.SysFont('monospace', 50).render(f'{SCORE1} - {SCORE2}', 1, BLACK)
    screen.blit(  # blit will only update on change
        scoreboard,
        (WIDTH / 2 - scoreboard.get_width() / 2, 10)
    )
    pygame.draw.circle(
        screen,  # on what
        GRAY,  # color
        # (WIDTH // 2, HEIGHT // 2),  # location
        (BALL_X, BALL_Y),
        RADIUS  # radius
    )

    p1 = pygame.draw.rect(
        screen,
        GREEN,
        (P1_X, P1_Y, P1_W, P1_H)  # location, x-width, y-length
    )
    p2 = pygame.draw.rect(
        screen,
        BLUE,
        (P2_X, P2_Y, P2_W, P2_H)  # location, x-width, y-length
    )
    pygame.display.update()
    CLOCK.tick(GAME_SPEED)

    # # for demo only
    # if pygame.key.get_pressed()[pygame.K_DOWN]:
    #     print(pygame.key.get_pressed()[pygame.K_DOWN])

    pressed = pygame.key.get_pressed()
    pygame.key.set_repeat()  # allow key repeat
    # player1 controls
    if pressed[pygame.K_r]:
        P1_Y -= PLAYER_SPEED
    elif pressed[pygame.K_f]:
        P1_Y += PLAYER_SPEED

    # player2 controls
    if pressed[pygame.K_UP]:
        P2_Y -= PLAYER_SPEED
    elif pressed[pygame.K_DOWN]:
        P2_Y += PLAYER_SPEED

    # ball movement
    BALL_X += SPEED_X
    BALL_Y += SPEED_Y
    
    # collisions
    # ball with screen
    if BALL_Y - RADIUS <= 0:  # ball top of screen
        SPEED_Y *= -1
    elif BALL_Y + RADIUS >= HEIGHT:  # ball bottom of screen
        SPEED_Y *= -1
    # player with screen
    if P1_Y < 0:  # player at top
        P1_Y = 0
    elif P1_Y + P1_H > HEIGHT:  # player at bottom
        P1_Y = HEIGHT - P1_H    
    if P2_Y < 0:  # player at top
        P2_Y = 0
    elif P2_Y + P2_H > HEIGHT:  # player at bottom
        P2_Y = HEIGHT - P2_H
    # player with ball
    if (BALL_X - RADIUS <= P1_X + P1_W and  # player and ball edge level
        P1_Y <= BALL_Y <= P1_Y + P1_H  # ball going to hit player
    ):
        SPEED_X *= -1
    if (BALL_X + RADIUS >= P2_X and  # player and ball edge level
        P2_Y <= BALL_Y <= P2_Y + P2_H  # ball going to hit player
    ):
        SPEED_X *= -1
    # goal
    if BALL_X <= 0 or BALL_X >= WIDTH:
        if BALL_X <= 0:
            SCORE2 += 1
            SPEED_X = abs(SPEED_X)
        else:
            SCORE1 += 1
            SPEED_X = -abs(SPEED_X)
        SPEED_Y = -abs(SPEED_Y)
        BALL_X = BALL_START_X
        BALL_Y = BALL_START_Y

    # exit?
    if pressed[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

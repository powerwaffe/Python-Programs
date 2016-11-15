import pygame, sys
from pygame.locals import *

# Sean Paoli
# 4/21/2016
# Simple pong-link game. Gameplay mechanics are simple, a higher score is gained when the user
# bounces the ball off their paddle, otherwise, it is reset to 0. The AI included deflects the ball
# every time.
# ---BUGS---
# Sometimes the ball phases through bottom and top portion of the main user's paddle


# number of frames per second, change to speed or slow the game
fps = 250
increaseSpeed = 2

# global variables to be used through program
windowWidth = 800
windowHeight = 600
lineThickness = 12
paddleSize = 110
paddleThickness = 20
paddleOffset = 20

# set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
paddleColor = (202, 150, 116)
gray = (132, 141, 134)
blue = (14, 47, 85)


# draws the arena the game will be played in
def draw_arena():
    displaySurf.fill(blue)

    # draw outline of arena
    pygame.draw.rect(displaySurf, white, ((0, 0), (windowWidth, windowHeight)), lineThickness * 2)

    # draw center line
    pygame.draw.line(displaySurf, white, ((windowWidth / 2), 0), ((windowWidth / 2),
                                                                  windowHeight), (int(lineThickness / 4)))


# draws the paddle
def draw_paddle(paddle):
    # stops paddle from moving too low
    if paddle.bottom > windowHeight - lineThickness:
        paddle.bottom = windowHeight - lineThickness

    # stops paddle from moving too high
    elif paddle.top < lineThickness:
        paddle.top = lineThickness

    # draws paddle
    pygame.draw.rect(displaySurf, paddleColor, paddle)


# draws the ball
def draw_ball(ball):
    pygame.draw.rect(displaySurf, white, ball)


# move the ball returns new position
def move_ball(ball, ball_dir_x, ball_dir_y):
    ball.x += ball_dir_x * increaseSpeed
    ball.y += ball_dir_y * increaseSpeed
    return ball


# checks for a collision with a wall, and 'bounces' ball off it
# returns new direction
def check_edge_collision(ball, ball_dir_x, ball_dir_y):
    if ball.top == lineThickness or ball.bottom == (windowHeight - lineThickness):
        ball_dir_y *= -1
    elif ball.left == lineThickness or ball.right == (windowWidth - lineThickness):
        ball_dir_x *= -1
    return ball_dir_x, ball_dir_y


# checks if the ball has hit a paddle and 'bounces' ball off it
def check_hit_ball(ball, paddle1, paddle2, ball_dir_x):
    if ball_dir_x == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > \
            ball.bottom:
        return -1
    elif ball_dir_x == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > \
            ball.bottom:
        return -1
    else:
        return 1


# checks to see if a point has been scored returns new score
def check_point_scored(paddle1, ball, score, ball_dir_x):

    # reset points if left wall is hit
    if ball.left == lineThickness:
        return 0
    # 1 point for hitting the ball
    elif ball_dir_x == -1 and paddle1.right == ball.left and paddle1.top < ball.top and ball.bottom < paddle1.bottom:
        score += 1
        return score

    # 5 points for beating the other paddle
    elif ball.right == windowWidth - lineThickness:
        score += 5
        return score

    # if no points scored, return score unchanged
    else:
        return score


# artificial intelligence of computer player
def artificial_intelligence(ball, ball_dir_x, paddle2):

    # if ball is moving away from paddle, center bat
    if ball_dir_x == -1:
        if paddle2.centery < (windowHeight / 2):
            paddle2.y += increaseSpeed
        elif paddle2.centery > (windowHeight / 2):
            paddle2.y -= increaseSpeed

    # if ball moving towards bat, track its movement
    elif ball_dir_x == 1:
        if paddle2.centery < ball.centery:
            paddle2.y += increaseSpeed
        else:
            paddle2.y -= increaseSpeed
    return paddle2


# displays the current score on the screen
def display_score(score):
    result_surf = basic_font.render('Score = %s' % score, True, white)
    result_rect = result_surf.get_rect()
    result_rect.topleft = (windowWidth - 120, 25)
    displaySurf.blit(result_surf, result_rect)


# main function
def main():
    pygame.init()
    global displaySurf

    # font information
    global basic_font, basic_font_size
    basic_font_size = 20
    basic_font = pygame.font.Font('freesansbold.ttf', basic_font_size)

    fps_clock = pygame.time.Clock()
    displaySurf = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Ping Pong')

    # initiate variable and set starting positions
    # any future changes made within rectangles
    ballX = windowWidth / 2 - lineThickness / 2
    ballY = windowHeight / 2 - lineThickness / 2
    playerOnePosition = (windowHeight - paddleSize) / 2
    playerTwoPosition = (windowHeight - paddleSize) / 2
    score = 0

    # keep track of ball direction
    ball_dir_x = -1  # -1 = left 1 = right
    ball_dir_y = -1  # -1 = up 1 = down

    # creates rectangles for ball and paddles
    paddle1 = pygame.Rect(paddleOffset, playerOnePosition, paddleThickness, paddleSize)
    paddle2 = pygame.Rect(windowWidth - paddleOffset - lineThickness, playerTwoPosition,
                          paddleThickness, paddleSize)
    ball = pygame.Rect(ballX, ballY, lineThickness, lineThickness)

    # draws the starting position of the arena
    draw_arena()
    draw_paddle(paddle1)
    draw_paddle(paddle2)
    draw_ball(ball)

    pygame.mouse.set_visible(0)  # make cursor invisible

    y = 0
    moveY = 0

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mouse movement commands
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                paddle1.y = mouse_y
            # keyboard commands
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    pass
                elif event.key == K_DOWN:
                    pass
            elif event.type == KEYUP:
                if event.key == K_UP:
                    moveY = 0
                elif event.key == K_DOWN:
                    moveY = 0

        y += moveY

        draw_arena()
        draw_paddle(paddle1)
        draw_paddle(paddle2)
        draw_ball(ball)

        ball = move_ball(ball, ball_dir_x, ball_dir_y)
        ball_dir_x, ball_dir_y = check_edge_collision(ball, ball_dir_x, ball_dir_y)
        score = check_point_scored(paddle1, ball, score, ball_dir_x)
        ball_dir_x *= check_hit_ball(ball, paddle1, paddle2, ball_dir_x)

        # AI paddle
        paddle2 = artificial_intelligence(ball, ball_dir_x, paddle2)

        # scoreboard
        display_score(score)

        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()

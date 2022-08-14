import pygame
from random import randint
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen = pygame.display.set_mode((1000, 1000))
direction = 0
move = [(-50, 0), (0, -50), (50, 0), (0, 50)]
snake = [[500, 500], [550, 500]]
clock = pygame.time.Clock()
game_over = False
fruit = [randint(1, 10) * 50, randint(1, 10) * 50]

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_a:
                direction = 0
            elif event.key == pygame.K_w:
                direction = 1
            elif event.key == pygame.K_d:
                direction = 2
            elif event.key == pygame.K_s:
                direction = 3

    snake[-1][0] = snake[0][0] + move[direction][0]
    snake[-1][1] = snake[0][1] + move[direction][1]
    temp = snake[-1]
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]
    snake[0] = temp
    if snake[0][0] < 0 or snake[0][0] > 1000 or snake[0][1] < 0 or snake[0][1] > 1000:
        game_over = True
    if snake[0] in snake[1:]:
        game_over = True
    if snake[0][0] == fruit[0] and snake[0][1] == fruit[1]:
        snake += [[fruit[0], fruit[1]]]
        while fruit in snake:
            fruit = [randint(1, 19) * 50, randint(1, 19) * 50]

    screen.fill(black)
    pygame.draw.circle(screen, red, fruit, 20)
    for i in range(len(snake)):
        pygame.draw.circle(screen, white, snake[i], 25)
    pygame.display.update()
    clock.tick(8)

pygame.quit()
quit()

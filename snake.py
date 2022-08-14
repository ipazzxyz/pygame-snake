import pygame
from random import randint
pygame.init()
pygame.font.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen = pygame.display.set_mode((1000, 1000))
direction = 0
move = [(-50, 0), (0, -50), (50, 0), (0, 50)]
snake = [[500, 500]]
game_over = False
fruit = [randint(2, 18) * 50, randint(2, 18) * 50]
count = 1

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_a and (direction == 1 or direction == 3):
                direction = 0
            elif event.key == pygame.K_w and (direction == 0 or direction == 2):
                direction = 1
            elif event.key == pygame.K_d and (direction == 1 or direction == 3):
                direction = 2
            elif event.key == pygame.K_s and (direction == 0 or direction == 2):
                direction = 3

    snake[-1][0] = snake[0][0] + move[direction][0]
    snake[-1][1] = snake[0][1] + move[direction][1]
    temp = snake[-1]
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]
    snake[0] = temp
    if snake[0][0] < 50 or snake[0][0] > 950 or snake[0][1] < 50 or snake[0][1] > 950:
        game_over = True
    if snake[0] in snake[1:]:
        game_over = True
    if snake[0][0] == fruit[0] and snake[0][1] == fruit[1]:
        count += 1
        snake += [[fruit[0], fruit[1]]]
        while fruit in snake:
            fruit = [randint(2, 18) * 50, randint(2, 18) * 50]
    screen.fill(black)
    pygame.draw.circle(screen, red, fruit, 20)
    for i in range(len(snake)):
        pygame.draw.circle(screen, white, snake[i], 25)
    pygame.draw.polygon(screen, red, [(0, 0), (0, 25), (1000, 25), (1000, 0)])
    pygame.draw.polygon(screen, red, [(0, 0), (25, 0), (25, 1000), (0, 1000)])
    pygame.draw.polygon(screen, red, [(1000, 1000), (975, 1000), (975, 0), (1000, 0)])
    pygame.draw.polygon(screen, red, [(1000, 1000), (1000, 975), (0, 975), (0, 1000)])
    screen.blit(pygame.font.Font(None, 36).render(str('x' + str(count)), True, white), (20, 20))
    pygame.display.update()
    pygame.time.Clock().tick(10)
print("Game ended with score ", count, "!", sep='')
pygame.quit()
quit()

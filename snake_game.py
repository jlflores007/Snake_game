import pygame, random

# Global variables
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SNAKE_SIZE = 20


def main():

    # Pygame Initialize
    pygame.init()

    # Set up for display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # To setup FPS
    clock = pygame.time.Clock()

    # Window's title
    pygame.display.set_caption('Snake Game')

    # Score
    score = 0
    font = pygame.font.SysFont(None, 36)

    # Snake
    snake = [pygame.Rect(100, 200, SNAKE_SIZE, SNAKE_SIZE)]
    snake_dir = pygame.K_d  # Start direction right

    # Food
    food = pygame.Rect(random.randint(0, (SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE, 
                       random.randint(0, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE, 
                       SNAKE_SIZE, SNAKE_SIZE)

    # Game Loop
    while True:

        screen.fill(COLOR_BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snake_dir != pygame.K_s:
                    snake_dir = pygame.K_w
                if event.key == pygame.K_s and snake_dir != pygame.K_w:
                    snake_dir = pygame.K_s
                if event.key == pygame.K_d and snake_dir != pygame.K_a:
                    snake_dir = pygame.K_d
                if event.key == pygame.K_a and snake_dir != pygame.K_d:
                    snake_dir = pygame.K_a

        # Move the snake
        if snake_dir == pygame.K_w:
            new_head = snake[0].move(0, -SNAKE_SIZE)
        elif snake_dir == pygame.K_s:
            new_head = snake[0].move(0, SNAKE_SIZE)
        elif snake_dir == pygame.K_a:
            new_head = snake[0].move(-SNAKE_SIZE, 0)
        elif snake_dir == pygame.K_d:
            new_head = snake[0].move(SNAKE_SIZE, 0)

        # Check for collision with walls
        if (new_head.left < 0 or new_head.right > SCREEN_WIDTH or
            new_head.top < 0 or new_head.bottom > SCREEN_HEIGHT):
            return  # End the game if snake collides with the wall

        # Check for collision with itself
        if new_head.collidelist(snake) != -1:
            return  # End the game if snake collides with itself
        
        # Snake grows
        snake.insert(0, new_head)

        # Check collision with food and reposition it
        if snake[0].colliderect(food):
            score += 10
            food.x = random.randint(0, (SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
            food.y = random.randint(0, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        else:
            # Remove the last segment of the snake
            snake.pop()

        # Renders the snake and food
        for pixel in snake:
            pygame.draw.rect(screen, COLOR_WHITE, pixel)
        pygame.draw.rect(screen, COLOR_WHITE, food)

        # Score system render
        score_text =  font.render(f'Score: {score}', True, COLOR_WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        # Controls the FPS
        clock.tick(10)


if __name__ == '__main__':
    main()
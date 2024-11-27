import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
paddle_width, paddle_height = 10, 100
player1_x, player1_y = 20, (height // 2) - (paddle_height // 2)
player2_x, player2_y = width - 30, (height // 2) - (paddle_height // 2)
paddle_speed = 7

# Ball settings
ball_size = 15
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5
ball_speed_y = 5

# Game loop control
running = True

# Main game loop
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < height - paddle_height:
        player2_y += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if (ball_x <= player1_x + paddle_width and player1_y <= ball_y <= player1_y + paddle_height) or \
       (ball_x >= player2_x - ball_size and player2_y <= ball_y <= player2_y + paddle_height):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds
    if ball_x < 0 or ball_x > width:
        ball_x, ball_y = width // 2, height // 2  # Reset ball position

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

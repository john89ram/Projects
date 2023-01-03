import pygame
pygame.init()

# Set the width and height of the screen
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Pong')

# Set the dimensions of the ball
ball_width, ball_height = 20, 20

# Set the initial position of the ball
ball_x, ball_y = screen_width // 2, screen_height // 2

# Set the initial velocity of the ball in the x and y directions
ball_vx, ball_vy = 5, 5

# Set the dimensions of the paddles
paddle_width, paddle_height = 20, 100

# Set the initial positions of the paddles
left_paddle_y = screen_height // 2
right_paddle_y = screen_height // 2

# Set the initial scores
left_score = 0
right_score = 0

# Set the font for displaying the scores
font = pygame.font.Font(None, 36)

# Set the game clock
clock = pygame.time.Clock()

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_x += ball_vx
    ball_y += ball_vy

    # Check if the ball has collided with the left or right walls
    if ball_x < 0 or ball_x + ball_width > screen_width:
        ball_vx = -ball_vx

    # Check if the ball has collided with the top or bottom walls
    if ball_y < 0 or ball_y + ball_height > screen_height:
        ball_vy = -ball_vy

    # Check if the ball has collided with the left paddle
    if ball_x < paddle_width and ball_y + ball_height > left_paddle_y and ball_y < left_paddle_y + paddle_height:
        ball_vx = -ball_vx

    # Check if the ball has collided with the right paddle
    if ball_x + ball_width > screen_width - paddle_width and ball_y + ball_height > right_paddle_y and ball_y < right_paddle_y + paddle_height:
        ball_vx = -ball_vx

    # Check if the ball has gone past the left paddle
    if ball_x < 0:
        right_score += 1
        ball_x, ball_y = screen_width // 2, screen_height // 2

    # Check if the ball has gone past the right paddle
    if ball_x + ball_width > screen_width:
        left_score += 1
        ball_x, ball_y = screen_width // 2, screen_height // 2

    # Draw the ball
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)

    # Draw the paddles
    pygame.draw.rect(screen, (255, 255, 255), (0, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (screen_width - paddle_width, right_paddle_y, paddle_width, paddle_height))

    # Get the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Move the left paddle up or down based on the keys
    if keys[pygame.K_w]:
        left_paddle_y -= 5
    if keys[pygame.K_s]:
        left_paddle_y += 5

    # Move the right paddle up or down based on the keys
    if keys[pygame.K_UP]:
        right_paddle_y -= 5
    if keys[pygame.K_DOWN]:
        right_paddle_y += 5

    # Ensure the paddles stay on the screen
    if left_paddle_y < 0:
        left_paddle_y = 0
    if left_paddle_y > screen_height - paddle_height:
        left_paddle_y = screen_height - paddle_height
    if right_paddle_y < 0:
        right_paddle_y = 0
    if right_paddle_y > screen_height - paddle_height:
        right_paddle_y = screen_height - paddle_height

    # Display the scores
    left_text = font.render(str(left_score), True, (255, 255, 255))
    right_text = font.render(str(right_score), True, (255, 255, 255))
    screen.blit(left_text, (screen_width // 2 - 50, 10))
    screen.blit(right_text, (screen_width // 2 + 30, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)
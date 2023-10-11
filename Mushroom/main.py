import pygame
from player import Player  # Import the Player class from player.py

pygame.init()

# Define window dimensions
window_width = 800
window_height = 600

# Create the Pygame display surface
screen = pygame.display.set_mode((window_width, window_height))

# Set the window caption
pygame.display.set_caption("MAARIOOOOO")

# Define the ground (a simple rectangle)
ground_color = (0, 128, 0)  # Green color (RGB)
ground_rect = pygame.Rect(0, window_height - 20, window_width, 20)  # 20 is the ground height

# Create a player object
player = Player(50, window_height - 50 - 20, 50, 50, window_height)

clock = pygame.time.Clock()  # Initialize Pygame's clock

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic
    keys = pygame.key.get_pressed()

    # Handle player movement
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    # Handle player jumping
    if keys[pygame.K_UP]:
        player.jump()

    # Update the player
    player.update()

    pygame.draw.rect(screen, player.color, player.get_rect())  # Draw the player

    # Rendering
    screen.fill((0, 0, 0))  # Clear the screen
    pygame.draw.rect(screen, ground_color, ground_rect)  # Draw the ground
    pygame.draw.rect(screen, player.color, player.rect)  # Draw the player

    pygame.display.update()  # Update the window

    clock.tick(60)  # Limit the frame rate to 60 frames per second

pygame.quit()

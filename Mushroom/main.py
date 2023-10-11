import pygame

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

# Define the character (a simple rectangle)
character_color = (255, 0, 0)  # Red color (RGB)
character_rect = pygame.Rect(50, window_height - 50 - 20, 50, 50)  # Character dimensions

# Character variables
character_speed = 5.0  # Adjust the speed as needed
character_x = character_rect.x
character_y = character_rect.y
character_y_speed = 0 #Initialize character's vertical speed
gravity = 0.5  # Adjust gravity as needed
jump_force = -10  # Adjust jump force as needed
is_jumping = False

clock = pygame.time.Clock()  # Initialize Pygame's clock

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed

    # Jumping logic
    if keys[pygame.K_SPACE] and not is_jumping:
        character_y_speed = jump_force
        is_jumping = True

    # Apply gravity
    character_y_speed += gravity
    character_y += character_y_speed

    # Collision with the ground
    if character_y >= window_height - 50 - 20:  # Adjust the collision condition
        character_y = window_height - 50 - 20  # Reset character to ground level
        character_y_speed = 0
        is_jumping = False

    # Update the character's rectangle position
    character_rect.x = character_x
    character_rect.y = character_y

    # Rendering
    screen.fill((0, 0, 0))  # Clear the screen
    pygame.draw.rect(screen, ground_color, ground_rect)  # Draw the ground
    pygame.draw.rect(screen, character_color, character_rect)  # Draw the character

    pygame.display.update()  # Update the window

    clock.tick(60)  # Limit the frame rate to 60 frames per second

pygame.quit()

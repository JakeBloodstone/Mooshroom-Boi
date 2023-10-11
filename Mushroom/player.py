import pygame

class Player:
    def __init__(self, x, y, width, height, window_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5.0
        self.y_speed = 0
        self.gravity = 0.5
        self.jump_force = -10
        self.is_jumping = False
        self.color = (255, 0, 0)  # Red color (RGB)
        self.window_height = window_height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # Create the player's rect

    def move_left(self):
        self.x -= self.speed
        self.rect.x = self.x

    def move_right(self):
        self.x += self.speed
        self.rect.x = self.x

    def jump(self):
        if not self.is_jumping:
            self.y_speed = self.jump_force
            self.is_jumping = True

    def update(self):
        # Implement collision and position updates here
        self.y_speed += self.gravity
        self.y += self.y_speed

        # Collision with the ground using self.window_height
        if self.y >= self.window_height - 50 - 20:  # Adjust the collision condition
            self.y = self.window_height - 50 - 20  # Reset player to ground level
            self.y_speed = 0
            self.is_jumping = False

        self.rect.y = self.y  # Update the rect's position

    def get_rect(self):
        return self.rect  # Getter method to retrieve the rect


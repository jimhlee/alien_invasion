import pygame

class Ship:
    # A class to manage the ship
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Pygame treats all game elements as rectangles(rect)
        self.screen_rect = ai_game.screen.get_rect()
        # Gets the ship's image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()


        # Store a decimal value of the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def update(self):
        # Update ship's position
        if self.moving_right and self.rect.right < self.screen_rect.right:    
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
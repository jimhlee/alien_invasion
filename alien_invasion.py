import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    # Overall class to manage game assets and behavior

    def __init__(self):
        # Initialize the game and create game resources
        pygame.init()
        self.settings = Settings()
        # Sets the size of the surface(screen)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

        '''
        For running in fullscreen mode instead:
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        '''

    def run_game(self):
        print('Game loop running')
        # Start main loop
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        # Responds to key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        # Responds to key releases 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def update_screen(self):
        # Resets the screen on each loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
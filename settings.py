class Settings:
    # Stores the settings for the game

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        # Sets background color in (R,G,B)
        # This is a light gray, hell yeah!
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 1.5

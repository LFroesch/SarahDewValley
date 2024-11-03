# Import pygame, constants, other files needed to run in main
import pygame, os, math, sys
import settings
from level import Level
from player import Player
os.environ['SDL_VIDEO_WINDOW_POS'] = "1920,0"

class Game:
    def __init__(self):

        
        #Pygame Init
        pygame.init()
        pygame.display.set_caption("Sarah Dew Valley")
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        print(f"Screen width: {settings.SCREEN_WIDTH}")
        print(f"Screen height: {settings.SCREEN_HEIGHT}")
        
        #Load Params
        print("Game Starting")

        # Print Start Game CLI Feed
        print("Key Index")
        print("-")
        print("Shift + Esc       = EXIT GAME")
        print("-")
        print("W | (UP ARROW)    = UP")
        print("S | (DOWN ARROW)  = DOWN")
        print("A | (LEFT ARROW)  = LEFT")
        print("D | (RIGHT ARROW) = RIGHT")
        print("-")
        print("Space             = Use Tool")
        print("Q                 = Change Tool")
        print("E                 = Change Seed")
        print("R                 = Use Seed")

        self.clock = pygame.time.Clock()
        self.level = Level()
        

    def run(self):
        # game loop & constants
        running = True
        while running:

            #event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #update check / loop
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()



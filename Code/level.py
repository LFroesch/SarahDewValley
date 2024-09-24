import pygame
import settings
from player import Player
from overlay import Overlay
from sprites import Generic

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup()
        self.setup()
        self.overlay = Overlay(self.player)
        #calling the setup on each init

    def setup(self):
        self.player = Player((640,360), self.all_sprites)
        Generic( 
            pos = (0,0),
            surf = pygame.image.load('../graphics/world/ground.png').convert_alpha(),
            groups =  self.all_sprites,
            z = settings.LAYERS['ground'])
        
    def run(self, dt):
        # update and draw the game
        self.display_surface.fill('black')
        #self.all_sprites.draw(self.display_surface)
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

        self.overlay.display()

#creating a special group where things spawn where camera is
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        # ??????????????????????
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        #???????????????????????
        
    def custom_draw(self, player):
        #???????????????????????
        self.offset.x = player.rect.centerx - settings.SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - settings.SCREEN_HEIGHT / 2
        
        #???????????????????????
        for layer in settings.LAYERS.values():
        #???????????????????????
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    #how does this work
                    self.display_surface.blit(sprite.image, offset_rect)
        
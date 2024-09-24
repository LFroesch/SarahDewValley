import pygame
from settings import *

class Overlay():
    def __init__(self,player):

        #general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        #imports - dictionaries with key/value pairs
        overlay_path = '../graphics/overlay/'
        #use this path to import overlay images
        self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools} #WHY PLAYER <----
        self.seeds_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.seeds}
        print(self.tools_surf)
        print(self.seeds_surf)
    
    def display(self):
        
        #tools
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
        #display tool w/ blit (x,y) or tool_rect pos
        self.display_surface.blit(tool_surf, tool_rect)
        
        #seeds
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom = OVERLAY_POSITIONS['seed'])
        self.display_surface.blit(seed_surf, seed_rect)
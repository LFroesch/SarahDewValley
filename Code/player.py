import pygame
from settings import *
from support import *
from timer import Timer
import sys

#make with pygame.sprite.Sprite because all Players will be sprites
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        #LOOK INTO THIS VVVVVVVVVV IMPORTING ASSETS 
        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0
        
        #draw/general pre-setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        ## ???
        self.z = LAYERS['main']

        #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 300

        #timers
        #look into this, it builds the dictionary that you use tools with
        self.timers = {
            'tool use': Timer(350, self.use_tool),
            'tool switch': Timer(200),
            'seed use': Timer(350, self.use_seed),
            'seed switch': Timer(200)
        }

        #tools
        #LOOK INTO THIS
        self.tools = ['hoe', 'axe', 'water']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]

        #seeds
        self.seeds = ['corn', 'tomato']
        self.seed_index = 0
        self.selected_seed = self.seeds[self.seed_index]

    def use_tool(self):
        # use the selected tool (future)
        pass

    def use_seed(self):
        # use the selected seed (future)
        pass

    def import_assets(self):

        # create dictionary of animations
        self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[]}
        
        # because it is out of folder
        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            # look into this what is this doing, assigning animations to the key?
            self.animations[animation] = import_folder(full_path)
        #print(self.animations)

    def animate(self, dt):
        #why 4 * dt?
        self.frame_index += 4 * dt
        if self.frame_index > len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]


    # Handle Key Presses as Input
    def input(self):

        # Key Index

        # Shift + Esc       = EXIT GAME

        # W | (UP ARROW)    = UP
        # S | (DOWN ARROW)  = DOWN
        # A | (LEFT ARROW)  = LEFT
        # D | (RIGHT ARROW) = RIGHT

        # Space             = Use Tool
        # Q                 = Change Tool
        # E                 = Change Seed
        # R                 = Use Seed

        
        keys = pygame.key.get_pressed()
        if not self.timers['tool use'].active:
            
            # Directional Movement
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s] or keys [pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0

            if keys[pygame.K_LSHIFT] and keys[pygame.K_ESCAPE]:
                sys.exit()

            # Tool Use
            if keys[pygame.K_SPACE] and not self.timers['tool use'].active:
                # if using a tool it activates the global cooldown 'gcd'
                self.timers['tool use'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0
                # CLI Output
                print(f"Using {self.selected_tool}")
            
            # Change Tools
            if keys[pygame.K_q] and not self.timers['tool switch'].active:
                # cooldown to swap tools
                self.timers['tool switch'].activate()
                self.tool_index += 1
                # if tool index > length of tools list => set tool index = 0
                self.tool_index = self.tool_index if self.tool_index < len(self.tools) else 0
                self.selected_tool = self.tools[self.tool_index]
                print(f"Swapped to {self.selected_tool}")

            # seed use
            if keys[pygame.K_r] and not self.timers['seed use'].active:
                # if using a seed it should use their like 'gcd'
                self.timers['seed use'].activate()
                # self.direction = pygame.math.Vector2()
                # self.frame_index = 0
                print(f'Planting {self.selected_seed} seed')

            # change seed
            if keys[pygame.K_e] and not self.timers['seed switch'].active:
                self.timers['seed switch'].activate()
                self.seed_index += 1
                # if seed index > length of seeds => set seed index = 0
                self.seed_index = self.seed_index if self.seed_index < len(self.seeds) else 0
                self.selected_seed = self.seeds[self.seed_index]
                print(f"Swapped to {self.selected_seed}")

    def get_status(self):

        # if the player is not moving, literally no motion/direction check with magnitude:
        if self.direction.magnitude() == 0:
        # IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
        # IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
        # add _idle to the status because _idle is the png name difference for animations
        # equalizes, not adds _idle only to the first part of the animation instead of x_idle_idle_idle_idle...
            self.status = self.status.split('_')[0] + '_idle'
        
        # tool use (FIX)
        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + "_" + self.selected_tool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def move(self, dt):
        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        # doing motion - look into this <--------
        # horizontal (x dimension) --FOR COLLISION!
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x #center x is self.pos.x
        # vertical (y dimension) --FOR COLLISION!
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y #center y is self.pos.y

    def update(self,dt):
        
        self.update_timers()
        self.get_status()
        self.input()
        self.move(dt)
        self.animate(dt)
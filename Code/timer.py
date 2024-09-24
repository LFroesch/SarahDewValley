import pygame

# REMEMBER KEEP IT SIMPLE :) SPLIT UP FUNCTIONS INTO EASIER FUNCTIONS

class Timer:
    def __init__(self,duration,func = None):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        #important !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #look into this !!!!
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        #check if you've passed timer
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time > self.duration:
            self.deactivate()
            if self.func:
                self.func()
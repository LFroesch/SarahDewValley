from os import walk
import pygame
#imports the ability to get to path

def import_folder(path):
    #init surface list to store all surfaces
    surface_list = []
    
    #for 'folder' and 'subfolder' w/e they may be ((LOOK INTO THIS))
    for _, __, img_files in walk(path):
        for image in img_files:
            #get full_path incl / 
            full_path = path + '/' + image
            print(full_path)
            #import pygame and load each image + convert it
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
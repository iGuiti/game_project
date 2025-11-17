import pygame
from menu import menu
from Const import Win_Width, Win_Height


class Game: 
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((Win_Width, Win_Height))


    def run(self):
        while True:

            menu_obj = menu(self.window)
            menu_obj.run()
            pass
                    

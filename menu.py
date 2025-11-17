import pygame as pg
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
from Const import Color_Orange, Win_Height, Win_Width, Menu_Option, Color_White



class menu:
    # Importar imagem e criando retangulo
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load("./asset/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    # Tocar música do menu
    def run(self):
        pg.mixer.music.load("./asset/Menu.mp3")
        pg.mixer_music.play(-1)

        # Atribuindo imagem ao retangulo e atualizar
        while True:
            self.window.blit(source = self.surf, dest = self.rect)
            self.text_menu(60, "Mountain", Color_Orange, (Win_Width/2, 70))
            self.text_menu(60, "Shooter", Color_Orange, (Win_Width/2, 120))

            for i in range(len(Menu_Option)):
                self.text_menu(30, Menu_Option[i], Color_White, (Win_Width/2, Win_Height/2 + 30 * i))

            pg.display.flip()

            #Check de eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() #Fechar janela
                    quit() #Finalizar Pygame

    def text_menu(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)



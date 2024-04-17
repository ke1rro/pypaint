import pygame
import constants
import drawfunction


class Color_Button():
    def __init__(self, color, button_position):
        self.surface = pygame.Surface((25, 25))
        self.surface = self.surface.convert()
        self.color = color
        self.surface.fill(self.color)
        self.rect = pygame.Rect(button_position)

    def is_mouse_over_btn(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_button_click(self):
        if self.color in constants.KEY_COLORS.values():
            for key, value in constants.KEY_COLORS.items():
                if value == self.color:
                    drawfunction.handle_mouse_events(key)
                    break


class Image_Button():
    def __init__(self, button_position, image, size=(50, 50)):
        self.size = size
        self.button_position = button_position
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = pygame.Rect(button_position)

    def is_mouse_over_btn(self,
                          image,
                          button_position, size=(0, 0, 50, 50), round=10):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.image, (158, 155, 147),
                             rect=size,
                             border_radius=round)
        else:
            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, size=self.size)
            self.rect = pygame.Rect(button_position)

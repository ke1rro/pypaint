import pygame
RUN = True
DOUBLECLICKTIME = 500
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
RED = (250, 0, 0)
MAROON = (128, 0, 0)
CRIMSON = (220, 20, 60)
SALMON = (250, 128, 128)
GREEN = (0, 250, 0)
DARK_GREEN = (1, 50, 32)
SPRING_GREEN = (0, 255, 127)
BLUE = (0, 0, 250)
AQUA = (0, 255, 255)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
OLIVE = (128, 128, 0)
ORANGE = (255, 127, 80)
BROWN = (139, 69, 19)
PURPLE = (128, 0, 128)
CURRENT_COLOR = WHITE
RGB_PALETTE_COLOR = WHITE
KEY_COLORS = {49: RED,
              50: BLUE,
              51: GREEN,
              52: BLACK,
              53: YELLOW,
              54: ORANGE,
              55: BROWN,
              56: DARK_GREEN,
              57: MAROON,
              58: CRIMSON,
              59: SALMON,
              60: GOLD,
              61: OLIVE,
              62: SPRING_GREEN,
              63: AQUA,
              64: PURPLE}
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 6)
RECT_CENTER_Y = RECT.centery // 2
PATH_IMG = 'images\\paint_icon.png'
PATH_ERASE_BTN = 'images\\eraser_pixel.png'
PATH_ARROW_UP = 'images\\arrow_up.png'
PATH_ARROW_DOWN = 'images\\arrow_down.png'
PATH_PALETTE = 'images\\palette.png'
PATH_BACK_BUTTON = 'images\\back_button.png'
PATH_APPLY_BUTTON = 'images\\apply_button.png'
PATH_CLOSE_BUTTON = 'images\\close_button.png'
CURRENT_RADIUS = 10
SCREEN_TEXT = "'Hold SHIFT' to see control buttons"
CONTROLS = ["'ESC' to EXIT",
            "'1-9' to pick corlors",
            "'CTRL' to enter color change mode",
            "'ENTER' in color change mode to apply color",
            "DOUBLE click erase button to erase the WHOLE back ground "
            ]
CONTROLS_FONT_COLOR = BLACK

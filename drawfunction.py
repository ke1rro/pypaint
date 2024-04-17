import pygame
import constants


def mouse_get_pos():
    mx, my = pygame.mouse.get_pos()
    return mx, my


def handle_key_events(event):
    constants.CURRENT_COLOR
    if event.key in constants.KEY_COLORS:
        constants.CURRENT_COLOR = constants.KEY_COLORS[event.key]


def handle_mouse_events(event):
    constants.CURRENT_COLOR
    if event in constants.KEY_COLORS:
        constants.CURRENT_COLOR = constants.KEY_COLORS[event]


def color_draw(surface):
    pygame.draw.circle(surface=surface,
                       color=((constants.CURRENT_COLOR)),
                       center=((mouse_get_pos())),
                       radius=constants.CURRENT_RADIUS)


def erase(surface):
    pygame.draw.circle(surface=surface,
                       color=((constants.WHITE)),
                       center=((mouse_get_pos())),
                       radius=100)


def draw_ui(surface):
    rect = pygame.Rect(0, 0,
                       constants.SCREEN_WIDTH,
                       constants.SCREEN_HEIGHT // 6)
    pygame.draw.rect(surface=surface, color=(127, 127, 127), rect=rect)
    rect_bottom = rect.y + rect.height
    pygame.draw.line(surface=surface,
                     color='black',
                     start_pos=(0, rect_bottom),
                     end_pos=(constants.SCREEN_WIDTH, rect_bottom), width=5)
    try:
        pygame.draw.circle(surface=surface,
                           color=constants.CURRENT_COLOR,
                           center=(rect.centerx, rect.centery),
                           radius=constants.CURRENT_RADIUS)
    except Exception as exc:
        print(f'DrawFunction wrong color {exc.args}')

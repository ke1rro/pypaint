import pygame
import constants
from buttons import Image_Button


def rgb_picker(screen, background):
    run = True
    bg2 = pygame.Surface(screen.get_size())
    bg2 = background.convert()
    bg2.fill(constants.WHITE)
    base_font = pygame.font.SysFont('segoeuiblack', 40,)
    rgb_font = pygame.font.SysFont('segoeuiblack', 50,)
    rgb_text = 'Choose color using RGB, for example RED - (255 0 0)'.upper()
    user_input_rgb = ''
    rgb_background_width = 600
    rgb_background_height = 600
    rgb_background_x = (constants.SCREEN_WIDTH - rgb_background_width) // 2
    rgb_background_y = (constants.SCREEN_HEIGHT - rgb_background_height + 70) // 2
    center_x = rgb_background_x + rgb_background_width // 2
    center_y = rgb_background_y + rgb_background_height // 2
    input_text_area = pygame.Rect(400, 430, 400, 75)

    apply_button = Image_Button(button_position=(650,
                                                 550,
                                                 200, 100),
                                image=constants.PATH_APPLY_BUTTON,
                                size=(200, 100))
    close_button = Image_Button(button_position=(350,
                                                 550,
                                                 200, 100),
                                image=constants.PATH_CLOSE_BUTTON,
                                size=(200, 100))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and user_input_rgb:
                    user_input_rgb = user_input_rgb[:-1]
                    bg2.fill(constants.WHITE)
                elif event.key == pygame.K_SPACE:
                    user_input_rgb += event.unicode
                elif event.key == pygame.K_RETURN:
                    try:
                        rgb = user_input_rgb.split()
                        rgb = [int(num) for num in rgb if num.strip()]
                        constants.RGB_PALETTE_COLOR = tuple(rgb)
                        constants.CURRENT_COLOR = constants.RGB_PALETTE_COLOR
                        run = False
                    except Exception as exc:
                        print(f'DrawFunction wrong color {exc.args}')
                else:
                    user_input_rgb += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if apply_button.rect.collidepoint(event.pos):
                    try:
                        rgb = user_input_rgb.split()
                        rgb = [int(num) for num in rgb if num.strip()]
                        constants.RGB_PALETTE_COLOR = tuple(rgb)
                        constants.CURRENT_COLOR = constants.RGB_PALETTE_COLOR
                    except Exception as exc:
                        print(f'DrawFunction wrong color {exc.args}')
                if close_button.rect.collidepoint(event.pos):
                    run = False

        Image_Button.is_mouse_over_btn(apply_button,
                                       button_position=apply_button.button_position,
                                       image=constants.PATH_APPLY_BUTTON,
                                       size=(0, 0, 200, 100),
                                       round=0)
        Image_Button.is_mouse_over_btn(close_button, button_position=close_button.button_position,
                                       image=constants.PATH_CLOSE_BUTTON,
                                       size=(0, 0, 200, 100),
                                       round=0)
        user_text_surface = rgb_font.render(user_input_rgb,
                                            True,
                                            (255, 255, 255))
        text_surface = base_font.render(rgb_text,
                                        True,
                                        (0, 0, 0))

        text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH // 2, 50))
        user_text_rect = user_text_surface.get_rect(center=(constants.SCREEN_WIDTH // 2,
                                                            constants.SCREEN_HEIGHT - 232.75))

        pygame.draw.rect(rect=(rgb_background_x,
                               rgb_background_y,
                               rgb_background_width,
                               rgb_background_height),
                         color=(127, 127, 127),
                         border_radius=2,
                         surface=bg2)

        pygame.draw.rect(rect=(rgb_background_x - 5,
                               rgb_background_y - 5,
                               rgb_background_width + 10,
                               rgb_background_height + 10),
                         color=(0, 0, 0),
                         border_radius=7,
                         width=5,
                         surface=bg2)

        pygame.draw.rect(rect=input_text_area,
                         color=(20, 20, 20),
                         border_radius=5,
                         surface=bg2)
        pygame.draw.rect(rect=user_text_rect,
                         color=(40, 40, 40),
                         border_radius=5,
                         surface=bg2)

        try:
            pygame.draw.circle(bg2,
                               constants.CURRENT_COLOR,
                               (center_x, center_y - 140),
                               150)
        except Exception as exc:
            print(f'DrawFunction wrong color {exc.args}')

        bg2.blit(apply_button.image, apply_button.button_position)
        bg2.blit(close_button.image, close_button.button_position)
        bg2.blit(text_surface, text_rect)
        bg2.blit(user_text_surface, user_text_rect)

        screen.blit(bg2, (0, 0))
        pygame.display.flip()

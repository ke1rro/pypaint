import pygame
import rgb_menu
import constants
import drawfunction
import pygame.locals
import button_config
from pygame.locals import *
from buttons import Color_Button, Image_Button

pygame.init()

FONT = pygame.font.SysFont('segoeuiblack', 14,)

clock = pygame.time.Clock()
doublelock = pygame.time.Clock()
window_icon = pygame.image.load(constants.PATH_IMG)
screen = pygame.display.set_mode((constants.SCREEN_WIDTH,
                                  constants.SCREEN_HEIGHT))

pygame.display.set_caption('PyPaint')
pygame.display.set_icon(window_icon)

bg = pygame.Surface(screen.get_size())
bg = bg.convert()
bg.fill(constants.WHITE)

controls_description = list(map(lambda x: FONT.render(x,
                                                      1,
                                                      constants.CONTROLS_FONT_COLOR),
                                constants.CONTROLS))

screen_text = FONT.render(constants.SCREEN_TEXT, True, constants.BLACK)

for btn_name, btn_color, btn_position in button_config.BUTTONS_INFO_LIST:
    button = Color_Button(color=btn_color, button_position=btn_position)
    button_config.BTN_DICT[btn_name] = button
for btn_name, btn_image, btn_position in button_config.IMG_BUTTONS_INFO_LIST:
    button = Image_Button(image=btn_image, button_position=btn_position)
    button_config.IMG_BTN_DICT[btn_name] = button


def run():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            constants.RUN = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
            rgb_menu.rgb_picker(screen=screen, background=bg)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
            for i, value in enumerate(controls_description):
                bg.blit(value, (290, 12 + i * 20))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            constants.RUN = False
        elif event.type == pygame.KEYDOWN:
            drawfunction.handle_key_events(event)
        elif pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[1] > 100:
            try:
                drawfunction.color_draw(bg)
            except Exception:
                print('Wrong Color')
        elif pygame.mouse.get_pressed()[2]:
            drawfunction.erase(bg)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_config.IMG_BTN_DICT['erase_button'].rect.collidepoint(event.pos):
                if doublelock.tick() < constants.DOUBLECLICKTIME:
                    bg.fill(constants.WHITE)
                else:
                    constants.CURRENT_COLOR = constants.WHITE
            elif button_config.IMG_BTN_DICT['arrow_up_button'].rect.collidepoint(event.pos):
                print('Pressed RADIUS UP')
                constants.CURRENT_RADIUS += 5
            elif button_config.IMG_BTN_DICT['arrow_down_button'].rect.collidepoint(event.pos):
                print('Pressed RADIUS DOWN')
                constants.CURRENT_RADIUS -= 5
            elif button_config.IMG_BTN_DICT['palette_button'].rect.collidepoint(event.pos):
                print('Pressed PALETTE')
                rgb_menu.rgb_picker(screen=screen, background=bg)
            else:
                for btn_name, button in button_config.BTN_DICT.items():
                    if button.rect.collidepoint(event.pos):
                        button.handle_button_click()
                        break
        screen.blit(bg, (0, 0))
        for btn_name, button in button_config.BTN_DICT.items():
            if button.is_mouse_over_btn():
                pygame.draw.rect(screen,
                                 (158, 155, 147),
                                 button.rect,
                                 border_radius=15)
            else:
                pygame.draw.rect(screen, button.color,
                                 button.rect,
                                 border_radius=15)
        for btn_name, button in button_config.IMG_BTN_DICT.items():
            screen.blit(button.image, button.rect.topleft)
        pygame.display.flip()


if __name__ == '__main__':
    while constants.RUN:
        clock.tick(10000)
        drawfunction.draw_ui(bg)
        bg.blit(screen_text, (930, 95))
        run()
        count = 0
        for btn_name, button in button_config.IMG_BTN_DICT.items():
            button_info = button_config.IMG_BUTTONS_INFO_LIST[count]
            Image_Button.is_mouse_over_btn(button,
                                           button_position=button_info[2],
                                           image=button_info[1])
            count += 1

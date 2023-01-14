import pygame


def draw_play_button(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Play!", True, (100, 255, 100))
    text_x = 400
    text_y = 250
    screen.blit(text, (text_x, text_y))

def draw_greetings(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Welcome, player!", True, (100, 255, 100))
    text_x = 300
    text_y = 150
    screen.blit(text, (text_x, text_y))


def draw_button_quit_d(screen):
    color_dark = (100, 100, 100)
    pygame.draw.rect(screen, color_dark, [width - 545, height - 200, 195, 40])


def draw_button_quit_l(screen):
    color_light = (170, 170, 170)
    pygame.draw.rect(screen, color_light, [width - 545, height - 200, 195, 40])


if __name__ == '__main__':
    pygame.init()
    smallfont = pygame.font.SysFont('Corbel', 35)
    text_quit = smallfont.render('Quit', True, (255, 255, 255))
    size = width, height = 900, 700
    screen = pygame.display.set_mode(size)
    draw_greetings(screen)
    draw_play_button(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if width - 480 <= mouse[0] <= width - 480 + 140 and height - 195 <= mouse[1] <= height - 195 + 40:
                    pygame.quit()
        mouse = pygame.mouse.get_pos()
        if width - 480 <= mouse[0] <= width - 480 + 140 and height - 195 <= mouse[1] <= height - 195 + 40:
            draw_button_quit_l(screen)
        else:
            draw_button_quit_d(screen)
        screen.blit(text_quit, (width - 480, height - 195))
        pygame.display.update()
    pygame.quit()
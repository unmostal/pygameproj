import pygame

def draw_greetings(screen):
    font = pygame.font.Font('ka1.ttf', 40)
    text = font.render("Welcome, player!", True, (100, 255, 100))
    text_x = 200
    text_y = 150
    screen.blit(text, (text_x, text_y))

def draw_play_button(screen):
    font = pygame.font.Font('ka1.ttf', 40)
    text = font.render("Play!", True, (100, 255, 100))
    text_x = 370
    text_y = 250
    screen.blit(text, (text_x, text_y))


def make_button_quit_d(screen):
    font = pygame.font.Font('ka1.ttf', 40)
    text = font.render("Quit", True, (100, 255, 100))
    text_x = 390
    text_y = 350
    screen.blit(text, (text_x, text_y))




if __name__ == '__main__':
    pygame.init()
    smallfont = pygame.font.SysFont('ka1.ttf', 35)
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
        # if width - 480 <= mouse[0] <= width - 480 + 140 and height - 195 <= mouse[1] <= height - 195 + 40:
        #     make_button_quit_l(screen)
        # else:
        make_button_quit_d(screen)
        pygame.display.update()
    pygame.quit()
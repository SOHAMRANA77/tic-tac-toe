import pygame
import sys
import TicTacToe as pvp
import AI as ai

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("R for Restart")

# Colors
BGcolor = (20, 189, 172)
black = (0, 0, 0)
button_color = (84, 84, 84)
hover_color = (242, 235, 211)

# Font
font = pygame.font.Font(None, 36)

# Button rectangles
button1_rect = pygame.Rect(40, 50, 150, 50)
button5_rect = pygame.Rect(140, 250, 150, 50)


def draw_button(x, y, width, height, text, hover):
    button_rect = pygame.Rect(x, y, width, height)
    color = hover_color if hover else button_color
    pygame.draw.rect(screen, color, button_rect)

    # Draw text on the button
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)


def main():
    running = True
    clock = pygame.time.Clock()
    ai_level_menu_visible = False
    ai_level_menu_rect = pygame.Rect(220, 50, 150, 50)  # Rectangle for the AI level menu
    PVP = False
    Ai = False
    R = False

    ai_l1_rect = None
    ai_l2_rect = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1_rect.collidepoint(pygame.mouse.get_pos()):
                    print("P V/S P clicked!")
                    Ai, R = False, False
                    PVP = True
                elif ai_level_menu_rect.collidepoint(pygame.mouse.get_pos()):
                    ai_level_menu_visible = not ai_level_menu_visible  # Toggle menu visibility
                elif ai_l1_rect and ai_l1_rect.collidepoint(pygame.mouse.get_pos()):
                    print("AI L1 clicked!")
                    R = True
                    Ai, PVP = False, False
                elif ai_l2_rect and ai_l2_rect.collidepoint(pygame.mouse.get_pos()):
                    print("AI L2 clicked!")
                    Ai = True
                    R, PVP = False, False
                elif button5_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Play clicked!")
                    if PVP:
                        screen.fill(BGcolor)
                        pvp.maingame()
                        pygame.display.flip()
                    elif R:
                        print("R")
                        screen.fill(BGcolor)
                        ai.main(0)
                        pygame.display.flip()
                    elif Ai:
                        print("Ai")
                        screen.fill(BGcolor)
                        ai.main(1)
                        pygame.display.flip()


        screen.fill(BGcolor)

        # Draw buttons
        draw_button(40, 50, 150, 50, "P V/S P", button1_rect.collidepoint(pygame.mouse.get_pos()))
        draw_button(140, 250, 150, 50, "Play", button5_rect.collidepoint(pygame.mouse.get_pos()))

        # Draw AI button and menu
        draw_button(220, 50, 150, 50, "AI", ai_level_menu_visible)
        if ai_level_menu_visible:
            ai_l1_rect = pygame.Rect(220, 110, 150, 50)
            ai_l2_rect = pygame.Rect(220, 170, 150, 50)
            draw_button(220, 110, 150, 50, "AI L1", ai_l1_rect.collidepoint(pygame.mouse.get_pos()))
            draw_button(220, 170, 150, 50, "AI L2", ai_l2_rect.collidepoint(pygame.mouse.get_pos()))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

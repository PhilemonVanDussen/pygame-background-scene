# Pygame game template

import pygame
import sys
import config # Import the config module
import random

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_rectangles(screen, color, rect, thickness):
    pygame.draw.rect(screen, color, rect, thickness)

def draw_circles(screen, color, center, radius, width):
    pygame.draw.circle(screen, color, center, radius, width)

def draw_ellipse(screen, color, rect, width):
    pygame.draw.ellipse(screen, color, rect, width)

def draw_line(screen, color, start_pos, end_pos, width):
    pygame.draw.line(screen, color, start_pos, end_pos, width)

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))


def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.BLACK) # Use color from config

        # Stars
        for offset in range(0, 800, 40):
           rect = [10 + offset, 20, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 80, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 140, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 200, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 260, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 320, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 380, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 440, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 500, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 560, 5, 5]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
        
         # Ring
        ellipse_rect = [110, 120, 600, 450]
        draw_ellipse(screen, (128, 128, 128), ellipse_rect, 5)
        
        # Sun
        center = (config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2)
        draw_circles(screen, (255, 174, 66), center, 100, 0 )
        
        # Planets
        draw_circles(screen, (0, 255, 255), (200, 150), 50, 0)
        draw_circles(screen, config.RED, (620, 470), 45, 0)
        draw_circles(screen, config.GREEN, (150, 450), 55, 0)
        draw_circles(screen, (157, 0, 255), (600, 150), 40, 0)

        # Details
        draw_line(screen, (0, 0, 139), (150, 150), (250, 150), 8)
        draw_circles(screen, (0, 100, 0,), (150, 450), 45, 0 )
        draw_circles(screen, (51, 0, 102), (600, 150), 30, 0)
        draw_line(screen, (255, 255, 0), (575, 470), (665, 470), 8)
        draw_circles(screen, (128, 128, 128), (120, 175), 20, 0 )

        # Text
        text_font = pygame.font.SysFont('Arial', 30)
        random_col = random.randrange(255), random.randrange(255), random.randrange(255)
        draw_text(screen, 'PJ VANDUSSSEN', text_font, random_col, 300, 150)


        pygame.display.flip()

        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()




# Pygame game template

import pygame
import sys
import config # Import the config module

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

def draw_ellipse(screen, color, x, y, width, height):
    pygame.draw.ellipse(screen, color, x, y, width, height)


def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.BLACK) # Use color from config

        # Stars
        for offset in range(0, 800, 40):
           rect = [10 + offset, 20, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 80, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 140, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 200, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 260, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 320, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 380, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 440, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 500, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
           rect = [10 + offset, 560, 10, 10]
           pygame.draw.rect(screen, config.WHITE, rect, 0)
        
        # Sun
        center = (config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2)
        draw_circles(screen, (255, 174, 66), center, 100, 0 )
        
        # Planets
        draw_circles(screen, config.BLUE, (200, 150), 50, 0)



        pygame.display.flip()

        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()




import pygame
from lib import pygame_plt as pgplot
import numpy as np

pygame.init()

WIDTH, HIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('Test of pygame_plot')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x_data = np.random.rand(5)*10
y_data = np.random.rand(5)*10

FPS = 1

def draw_window():
    '''Sets background color to white'''
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False

        draw_window()
        plt = pgplot.Plot(surface=WIN)
        plt.position(0, 600, 0, 600)

        plt.scatter(x=x_data, y=y_data)

    pygame.quit()

if __name__ == '__main__':
    main()

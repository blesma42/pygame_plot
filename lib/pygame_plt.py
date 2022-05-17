import pygame
import coordinate_converter as cc
import fit
import position
import x_axis
import y_axis
import mouse_position
import scatter

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

class Plot:
    def __init__(self, surface: pygame.Surface):
        
        self.background = WHITE
        
        self.surface=surface
        
        # where plot will be placed within the pygame window
        self.position(top=0, bottom=200, left=0, right=200)

        # axis formats
        self.x_limits(min=0, max=10)
        self.y_limits(min=0, max=10)

        self.x_ticks = 10
        self.y_ticks = 10

        self.font_size = 12
        
        self.x_axis()
        self.y_axis()
        
        self.mouse_tracker()

    def position(self, top: int, bottom: int, left: int, right: int):
        '''Sets the position of the plot within the pygame window. Requires four arguments in pygame coordinates: top, bottom, left, right'''
        position.position(self, top, bottom, left, right)      
    
    def x_limits(self, min: float, max: float):
        '''Sets the limits of the x-axis. Requires two arguments: min, max.'''
        self.x_min=min
        self.x_max=max
        self.x_range=self.x_max-self.x_min

    def y_limits(self, min: float, max: float):
        '''Sets the limits of the y-axis. Requires two arguments: min, max.'''
        self.y_min=min
        self.y_max=max
        self.y_range=self.y_max-self.y_min

    def fit(self, scaling_factor: float=0.8):
        '''Scales the plot by the given factor.'''
        fit.fit(self, scaling_factor)

    def coords(self, x, y):
        '''Convertes regular grid coordinates to pygame coordinates'''
        return cc.coords(self, x, y)

    def coords_reversed(self, x, y):
        '''Convertes pygame coordinates to grid coordinates'''
        return cc.coords_reversed(self, x, y)

    def x_axis(self):
        '''Creates and formats x_axis.'''
        self.x_axis = x_axis.x_axis(self, min=self.x_min, max=self.x_max, ticks=self.x_ticks)
    
    def y_axis(self):
        '''Creates and formats y_axis.'''
        self.y_axis = y_axis.y_axis(self, min=self.y_min, max=self.y_max, ticks=self.y_ticks)

    def x_grid(self, draw=True, number_of_lines=10, color=BLACK):
        '''Draws grid on x-axis''' 
        self.x_axis.grid(draw, number_of_lines, color)

    def y_grid(self, draw=True, number_of_lines=10, color=BLACK):
        '''Draws grid on y-axis'''   
        self.y_axis.grid(draw, number_of_lines, color)
     
    def mouse_tracker(self, show=False, font='arial', font_size=12, font_color=BLACK, background_color=ORANGE, distance=30):
        self.mouse_position_tracker = mouse_position.mouse_tracker(self, show, font, font_size, font_color, background_color, distance)

    def scatter(self, x, y, shape='cross', color=BLUE, size=10):
        '''Draws an scatter plot from given x and y. x and y must be iterables with equal lenght.'''
        scatter.scatter(self, x, y, shape='cross', color=BLUE, size=10)

    def general_elements(self):
        '''Draws general elements of the plot, like axis, and grid.'''

        self.x_axis.draw()
        self.y_axis.draw()
        self.mouse_position_tracker.draw()

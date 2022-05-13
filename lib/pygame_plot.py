import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Plot:
    def __init__(self, surface: pygame.Surface):
        self.background = WHITE
        
        self.surface=surface
        
        # where plot will be placed within the pygame window
        self.position(top=0, bottom=200, left=0, right=200)

        # axis formats
        self.x_limits(min=0, max=10)
        self.y_limits(min=0, max=10)

        self.x_major_ticks(number_of_ticks=10)
        self.y_major_ticks(number_of_ticks=10)

        self.font_size = 12

    def position(self, top: int, bottom: int, left: int, right: int):
        '''Sets the position of the plot within the pygame window. Requires four arguments in pygame coordinates: top, bottom, left, right'''
        self.given_top = top
        self.given_bottom = bottom
        self.given_left = left
        self.given_right = right
        self.given_hight = self.given_bottom-self.given_top
        self.given_width = self.given_right-self.given_left 

        self.fit()          
    
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

    def x_major_ticks(self, number_of_ticks: int):
        '''Number of major ticks on x-axis. First tick will be placed at x_min, last at x_max.'''
        self.number_of_x_major_ticks=number_of_ticks
    
    def y_major_ticks(self, number_of_ticks: int):
        '''Number of major ticks on y-axis. First tick will be placed at y_min, last at y_max.'''
        self.number_of_y_major_ticks=number_of_ticks

    def fit(self, scaling_factor: float=0.8):
        '''Scales the plot by the given factor.'''
        self.scaling_factor = scaling_factor
        self.top = self.given_top-(1-self.scaling_factor)/2*self.given_hight
        self.bottom = self.given_bottom-(1-self.scaling_factor)/2*self.given_hight
        self.left = self.given_left+(1-self.scaling_factor)/2*self.given_width
        self.right = self.given_right-(1-self.scaling_factor)/2*self.given_width
        self.hight = self.given_hight*self.scaling_factor
        self.width = self.given_width*self.scaling_factor

    def coords(self, x, y):
        '''Convertes regular grid coordinates to pygame coordinates'''
        self.x_shift = self.left
        
        self.x_unit = self.width/self.x_range
        self.y_unit = self.hight/self.y_range

        x_scaled = (x-self.x_min)*self.x_unit+self.x_shift
        y_scaled = (y-self.y_min)*self.y_unit

        return (x_scaled, self.bottom-y_scaled)
            
    def coordinate_system(self):
        '''Draws a coordinate system (x- and y-axis)'''
        self.origin = self.coords(self.x_min, self.y_min) # sets bottem left corner of the coordinate system where axis intersect
        
        # axis should be longer longer than value range, hence added range*0.05
        self.x_axis_end = self.coords(self.x_max+self.x_range*0.1, self.y_min)
        self.y_axis_end = self.coords(self.x_min, self.y_max+self.y_range*0.1)

        pygame.draw.line(self.surface, BLACK, self.origin, self.x_axis_end) # x-axis
        pygame.draw.line(self.surface, BLACK, self.origin, self.y_axis_end) # y-axis

        # arrows at the end of the axis
        arrow_size = 10
        pygame.draw.polygon(self.surface, BLACK, [self.x_axis_end, (self.x_axis_end[0]-arrow_size, self.x_axis_end[1]-arrow_size//2), (self.x_axis_end[0]-arrow_size, self.x_axis_end[1]+arrow_size//2)]) # x axis arrow
        pygame.draw.polygon(self.surface, BLACK, [self.y_axis_end, (self.y_axis_end[0]+arrow_size//2, self.y_axis_end[1]+arrow_size), (self.y_axis_end[0]-arrow_size//2, self.y_axis_end[1]+arrow_size)]) # y axis arrow

    def x_ticks(self, number_of_ticks, length=5, lable=True):
        '''Draws ticks on x-axis and lables them.'''
        if number_of_ticks==0:
            return
        for i in range(number_of_ticks+1):
            # draws ticks
            x_start = self.coords(self.x_range/number_of_ticks*i+self.x_min, self.y_min)

            pygame.draw.line(self.surface, BLACK, x_start, (x_start[0], x_start[1]+length)) 
            
            if lable==True:
                # lables ticks
                text_x = str(round(i/number_of_ticks*self.x_range+self.x_min, 1))
                font = pygame.font.SysFont('arial', self.font_size)
                text = font.render(text_x, True, BLACK, WHITE)
                textRect = text.get_rect()
                textRect.center = (x_start[0], x_start[1]+length*2)
                self.surface.blit(text, textRect)

    def y_ticks(self, number_of_ticks, length=5, lable=True):
        '''Draws ticks on y-axis and lables them. '''
        if number_of_ticks==0:
            return
        for i in range(number_of_ticks+1):
            # draws ticks
            y_start = self.coords(self.x_min, self.y_range/number_of_ticks*i+self.y_min)

            pygame.draw.line(self.surface, BLACK, y_start, (y_start[0]-length, y_start[1]))

            if lable==True:
                # lables ticks
                text_y = str(round(i/number_of_ticks*self.y_range+self.y_min, 1))
                font = pygame.font.SysFont('arial', self.font_size)
                text = font.render(text_y, True, BLACK, WHITE)
                textRect = text.get_rect()
                textRect.center = (y_start[0]-length*2, y_start[1])
                self.surface.blit(text, textRect)

    def x_major_grid(self, color, draw=True):
        '''Draws the major x-grid if draw=True. Gridlines are drawn at same position as x-ticks.'''
        if draw==False:
            return
        self.x_grid(self.number_of_x_major_ticks, color)

    def x_grid(self, number_of_lines, color):
        '''Draws grid on x-axis'''   
        for i in range(number_of_lines+1):
            start = self.coords(self.x_range/number_of_lines*i+self.x_min, self.y_min)
            end = self.coords(self.x_range/number_of_lines*i+self.x_min, self.y_max)
            pygame.draw.line(self.surface, color, start, end) 

    def y_major_grid(self, color, draw=True):
        '''Draws the major y-grid if draw=True. Gridlines are drawn at same position as y-ticks.'''
        if draw==False:
            return
        self.y_grid(self.number_of_y_major_ticks, color)

    def y_grid(self, number_of_lines, color):
        '''Draws grid on y-axis'''   
        for i in range(number_of_lines+1):
            start = self.coords(self.x_min, self.y_range/number_of_lines*i+self.y_min)
            end = self.coords(self.x_max, self.y_range/number_of_lines*i+self.y_min)
            pygame.draw.line(self.surface, color, start, end) 
            
    def scatter(self, x, y, shape='cross', color=BLUE, size=10):
        '''Draws an scatter plot from given x and y. x and y must be iterables with equal lenght.'''
        
        def draw_point(x, y, shape, color, size):
            '''Draws a point at the given coordinates. Coordinates need to be a 2-dimensional iterable (tuple, list, ...) in coordinate system valuses (not pygame values). '''
            center = self.coords(x, y)
            radius = 4
            if shape == 'cross':
                # cross is made from two indipendent lines crossing each other
                line1_start = (center[0]-size/2, center[1]-size/2)
                line2_start = (center[0]-size/2, center[1]+size/2)
                line1_end = (center[0]+size/2, center[1]+size/2)
                line2_end = (center[0]+size/2, center[1]-size/2)
                pygame.draw.line(self.surface, color, line1_start, line1_end)
                pygame.draw.line(self.surface, color, line2_start, line2_end)
            elif shape == 'circle':
                pygame.draw.circle(self.surface, color, center, radius)
            elif shape == 'square':
                left = center[0]-size/2
                top = center[1]-size/2
                width = size
                height = size
                pygame.draw.rect(self.surface, color, [left, top, width, height])
            elif shape == 'triangle':
                h = 3**0.5/2*size # formula for height of a isosceles triangles
                top = (center[0], center[1]-h/2)
                left = (center[0]-size/2, center[1]+h/2)
                right = (center[0]+size/2, center[1]+h/2)
                pygame.draw.polygon(self.surface, color, [top, left, right])
            else:
                raise ValueError(f'<{shape}> is not a valid shape. Try cross, square, or triangle.')
        
        if len(x) != len(y):
            raise ValueError('Input data x and y must be of equal lenght.')

        self.general_elements()

        self.x_data = x
        self.y_data = y

        for i in range(len(x)):
            draw_point(x[i], y[i], shape, color, size)

        pygame.display.update()

    def general_elements(self):
        '''Draws general elements of the plot, like axis, and grid.'''
        self.coordinate_system()
        self.x_ticks(self.number_of_x_major_ticks)
        self.y_ticks(self.number_of_y_major_ticks)
        self.x_major_grid(color=GREY, draw=True)
        self.y_major_grid(color=GREY, draw=True)


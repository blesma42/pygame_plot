import pygame

def scatter(self, x, y, shape, color, size):
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
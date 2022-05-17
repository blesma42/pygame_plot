import pygame
import warnings

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class x_axis:
    '''Will handle everything related to the x_axis, like range of the axis, ticks, grid, and foramtting.'''
    def __init__(self, plt, min=0, max=10, ticks=10, tick_length=10, width=1, color=BLACK):
        
        self.plt = plt
        self.y_min = self.plt.y_min
        self.y_max = self.plt.y_max

        self.x_min = min
        self.x_max = max
        self.number_of_ticks = ticks
        self.tick_length = tick_length
        self.width  = width

        self.color = color

        self.ticks()
        self.tick_lable()
        self.lable()
        self.grid()
    
    def calc_range(self):
        self.range = self.x_max-self.x_min
    
    def draw_axis(self):
        self.calc_range()

        self.origin = self.plt.coords(self.x_min, self.y_min) # sets bottem left corner of the coordinate system where axis intersect
        
        # axis should be longer longer than value range, hence added range*0.05
        self.end = self.plt.coords(self.x_max+self.range*0.1, self.y_min)

        pygame.draw.line(self.plt.surface, self.color, self.origin, self.end, self.width) # x-axis

        # arrows at the end of the axis
        arrow_size = 10
        pygame.draw.polygon(self.plt.surface, self.color, [self.end, (self.end[0]-arrow_size, self.end[1]-arrow_size//2), (self.end[0]-arrow_size, self.end[1]+arrow_size//2)]) # x axis arrow    

    def ticks(self, draw=True, number_of_ticks=10, length=10, size=1, shift=0):
        self.tick_draw = draw   
        self.number_of_ticks = number_of_ticks
        self.tick_length = length
        self.tick_size = size
        self.tick_shift = shift

    def draw_ticks(self):
        if self.tick_draw == False: return

        for i in range(self.number_of_ticks+1):
            # draws ticks
            position = self.plt.coords(self.range/self.number_of_ticks*i+self.x_min, self.y_min)
            start = (position[0], position[1]+self.tick_shift)
            end = (start[0], start[1]+self.tick_length)

            pygame.draw.line(self.plt.surface, self.color, start, end, self.width) 
         
    def tick_lable(self, font='arial', size=12, color=BLACK, background=WHITE):
        self.tick_font = font
        self.tick_font_size = size
        self.tick_font_color = color
        self.tick_font_background_color = background

    def draw_tick_lable(self):
        if self.tick_draw == False: return

        font_formatted = pygame.font.SysFont(self.tick_font, self.tick_font_size)
        for i in range(self.number_of_ticks+1):
            text_to_show = str(round(i/self.number_of_ticks*self.range+self.x_min, 1))
            text = font_formatted.render(text_to_show, True, self.tick_font_color, self.tick_font_background_color)
            textRect = text.get_rect()
            position = self.plt.coords(self.range/self.number_of_ticks*i+self.x_min, self.y_min)
            textRect.center = (position[0], position[1]+2*self.tick_length)

            self.plt.surface.blit(text, textRect)
    
    def grid(self, draw=True, number_of_lines=10, color=BLACK):
        '''Draws grid on x-axis''' 
        self.grid_draw=draw
        self.grid_number_of_lines = number_of_lines
        self.grid_color = color

    def draw_grid(self):
        if self.grid_draw == False: return
        
        for i in range(self.grid_number_of_lines+1):
            start = self.plt.coords(self.range/self.grid_number_of_lines*i+self.x_min, self.y_min)
            end = self.plt.coords(self.range/self.grid_number_of_lines*i+self.x_min, self.y_max)
            pygame.draw.line(self.plt.surface, self.grid_color, start, end)

    def lable(self, draw=True, text='x', font='arial', size=12, color=BLACK, background=WHITE):
        self.lable_draw = draw
        self.lable_text = str(text)
        self.lable_font = font
        self.lable_font_size = size
        self.lable_font_color = color
        self.lable_font_background_color = background

    def draw_lable(self):
        if self.lable_draw == False: return

        font_formatted = pygame.font.SysFont(self.lable_font, self.lable_font_size)
        text_to_show = str(self.lable_text)
        text = font_formatted.render(text_to_show, True, self.lable_font_color, self.lable_font_background_color)
        textRect = text.get_rect()
        position = self.plt.coords(self.range/2+self.x_min, self.y_min)
        textRect.center = (position[0], position[1]+4*self.tick_length)

        self.plt.surface.blit(text, textRect)
    
    def error_handling(self):
        if self.number_of_ticks == 0:
            warnings.warn('number_of_ticks=0. This is evaluated as draw=False.')
            self.tick_draw = False
        if self.number_of_ticks < 0:
            self.number_of_ticks = self.number_of_ticks*-1
            warnings.warn(f'number_of_ticks was negeative, set to {self.number_of_ticks}.')

        if self.grid_number_of_lines == 0:
            warnings.warn('grid_number_of_lines=0. This is evaluated as draw=False.')
            self.grid_draw = False
        if self.grid_number_of_lines < 0:
            self.grid_number_of_lines = self.grid_number_of_lines*-1
            warnings.warn(f'grid_number_of_lines was negeative, set to {self.grid_number_of_lines}.')

        if len(self.lable_text) == 0:
            warnings.warn(f'No text for x-axis lable was given.')

    def draw(self):
        self.error_handling()
        self.draw_axis()
        self.draw_ticks()
        self.draw_tick_lable()
        self.draw_lable()
        self.draw_grid()

    



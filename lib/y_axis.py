import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class y_axis:
    def __init__(self, plt, min=0, max=10, ticks=10, tick_length=10, width=1, color=BLACK):
        
        self.plt = plt
        self.x_min = self.plt.x_min
        self.x_max = self.plt.x_max

        self.y_min = min
        self.y_max = max
        self.number_of_ticks = ticks
        self.tick_length = tick_length
        self.width  = width

        self.color = color

        self.ticks()
        self.tick_lable()
        self.grid()
    
    def calc_range(self):
        self.range = self.y_max-self.y_min
    
    def draw_axis(self):
        self.calc_range()

        self.origin = self.plt.coords(self.x_min, self.y_min) # sets bottem left corner of the coordinate system where axis intersect
        
        # axis should be longer longer than value range, hence added range*0.05
        self.end = self.plt.coords(self.x_min, self.y_max+self.range*0.1)

        pygame.draw.line(self.plt.surface, self.color, self.origin, self.end, self.width) # x-axis

        # arrows at the end of the axis
        arrow_size = 10
        pygame.draw.polygon(self.plt.surface, self.color, [self.end, (self.end[0]+arrow_size//2, self.end[1]+arrow_size), (self.end[0]-arrow_size//2, self.end[1]+arrow_size)]) # y axis arrow

    def ticks(self, draw=True, number_of_ticks=10, length=10, size=1, shift=0):
        self.tick_draw = draw
        if self.tick_draw == False: return
        if number_of_ticks==0: return
        if length == 0: return
        if size == 0: return

        self.number_of_ticks = number_of_ticks
        self.tick_length = length
        self.tick_size = size
        self.tick_shift = shift

    def draw_ticks(self):
        if self.tick_draw == False: return

        for i in range(self.number_of_ticks+1):
            # draws ticks
            position = self.plt.coords(self.x_min, self.range/self.number_of_ticks*i+self.y_min)
            start = (position[0]+self.tick_shift, position[1])
            end = (start[0]-self.tick_length, start[1])

            pygame.draw.line(self.plt.surface, self.color, start, end, self.width) 
         
    def tick_lable(self, font='arial', size=12, color=BLACK, background=WHITE):
        self.tick_font = font
        self.tick_font_size = size
        self.tick_font_color = color
        self.tick_font_background_color = background

    def draw_tick_lable(self):
        font_formatted = pygame.font.SysFont(self.tick_font, self.tick_font_size)
        for i in range(self.number_of_ticks+1):
            text_to_show = str(round(i/self.number_of_ticks*self.range+self.y_min, 1))
            text = font_formatted.render(text_to_show, True, self.tick_font_color, self.tick_font_background_color)
            textRect = text.get_rect()
            position = self.plt.coords(self.x_min, self.range/self.number_of_ticks*i+self.y_min)
            
            textRect.center = (position[0]+self.tick_shift-2*self.tick_length, position[1])

            self.plt.surface.blit(text, textRect)

    def grid(self, draw=True, number_of_lines=10, color=BLACK):
        '''Draws grid on x-axis''' 
        self.grid_draw=draw

        if self.grid_draw == False: return
        if number_of_lines == 0: return

        self.grid_number_of_lines = number_of_lines
        self.grid_color = color

    def draw_grid(self):
        if self.grid_draw == False: return
        
        for i in range(self.grid_number_of_lines+1):
            start = self.plt.coords(self.x_min, self.range/self.grid_number_of_lines*i+self.y_min)
            end = self.plt.coords(self.x_max, self.range/self.grid_number_of_lines*i+self.y_min)
            pygame.draw.line(self.plt.surface, self.grid_color, start, end)

    def draw(self):
        self.draw_axis()
        self.draw_ticks()
        self.draw_tick_lable()
        self.draw_grid()
        

    
    



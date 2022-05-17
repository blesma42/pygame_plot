import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class mouse_tracker:
    '''Tracks mouse and shows current position in coordinate values.''''''
    def __init__(self, plot, show, font, font_size, font_color, background_color, distance):
        self.plt = plot
        self.show_mouse_position = show
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.distance = distance

    def get_position(self):
        # gets the current position
        self.mouse_current_position = pygame.mouse.get_pos()
        self.coordinate_position = self.plt.coords_reversed(self.mouse_current_position[0], self.mouse_current_position[1])

    def draw(self):
        # displays vcurrent position
        if self.show_mouse_position == False: return

        self.get_position()

        if self.coordinate_position[0]<self.plt.x_min or self.coordinate_position[0]>self.plt.x_max:
            return
        if self.coordinate_position[1]<self.plt.y_min or self.coordinate_position[1]>self.plt.y_max:
            return

        font_formatted = pygame.font.SysFont(self.font, self.font_size)
        text_to_show = str(self.coordinate_position)
        text = font_formatted.render(text_to_show, True, self.font_color, self.background_color)
        textRect = text.get_rect()
        textRect.center = (self.mouse_current_position[0]+self.distance, self.mouse_current_position[1]+self.distance)

        self.plt.surface.blit(text, textRect)

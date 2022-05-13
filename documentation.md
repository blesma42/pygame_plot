# pygame_plot documentation

The pygame_plot function creates plots within pygame and draws them on a given pygame surface.

--------------------------

    import pygame
    import pygame_plot as pgplot

    pygame.init()

    WIDTH, HIGHT = 600, 600
    WIN = pygame.display.set_mode((WIDTH, HIGHT))

    x_data = [1, 2, 3, 4, 5]
    y_data = [1, 2, 3, 4, 5]

    WHITE = (255, 255, 255)

    FPS = 1

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        pygame.display.update()

        plt = pgplot.Plot(surface=WIN)
        plt.scatter(x=x_data, y=y_data)

    pygame.quit()

--------------------------

|Function|Description|
|-|-|
|Plot(surface)|Initilizes a plot on the given surface. Must be type pygame.Surface|
|Plot.position(top: int, bottom: int, left: int, right: int)|Position of the plot in the surface. All arguments must be given in pygame coordinates.|
|Plot.x_limits(min: float, max: float)|Limits of the x_axis. Must be numeric.|
|Plot.y_limits(min: float, max: float)|Limits of the y_axis. Must be numeric.|
|Plot.x_major_ticks(number_of_ticks: int)|Sets number of major x-ticks|
|Plot.y_major_ticks(number_of_ticks: int)|Sets number of major y-ticks|
|Plot.fit(scaling_factor: float)|Scales plot down or up. If scaling_factor=1 the x- and y-axis allign with the positions given by Plot.position.|
|Plot.coords(x, y)|Converts a coordinate point into pygame coordinates in respect to the position of the plot and the axis scales. Returnes the pygame coordinates as touple.|
|Plot.coordinate_system()|Draws the x- and y-axis with an arrow at there end.|
|Plot.x_ticks(number_of_ticks, length=5, lable=True)|Draws ticks on x-axis. The number of ticks is given by number_of_ticks. First tick is placed at the x_min, last at x_max. If lable=True ticks are labled.|
|Plot.y_ticks(number_of_ticks, length=5, lable=True)|Draws ticks on y-axis. The number of ticks is given by number_of_ticks. First tick is placed at the y_min, last at y_max. If lable=True ticks are labled.|
|Plot.x_major_grid(color, draw=True)|Adds grid lines parallel to the y-axis. x-position of these lines is the same as of the x-ticks. If draw=False lines are not drawn.|
|Plot.x_grid(number_of_lines, color)|Add grid lines parallel to y-axis. x-position is calculated based on x_min, x_max, and number_of_lines.|
|Plot.y_major_grid(color, draw=True)|Adds grid lines parallel to the x-axis. x-position of these lines is the same as of the y-ticks. If draw=False lines are not drawn.|
|Plot.y_grid(number_of_lines, color)|Add grid lines parallel to x-axis. y-position is calculated based on y_min, y_max, and number_of_lines|
|Plot.scatter(x, y, shape='cross', color=BLUE, size=10)|Populates the coordinate system with points. x and y must be iterables (list, array, ...) with the coordianates of the points. shape sets the shape used to draw the points. Availible are 'cross', 'circle', 'square', 'triangle'.|
|Plot.general_elements()|Function will call several other functions (Plot.coordinate_system(), tick functions, and grid functions) to generate the plot.|

def position(self, top: int, bottom: int, left: int, right: int):
    '''Sets the position of the plot within the pygame window. Requires four arguments in pygame coordinates: top, bottom, left, right'''
    self.given_top = top
    self.given_bottom = bottom
    self.given_left = left
    self.given_right = right
    self.given_hight = self.given_bottom-self.given_top
    self.given_width = self.given_right-self.given_left 

    self.fit()    
def coords(self, x, y):
    '''Convertes regular grid coordinates to pygame coordinates.'''  
    self.x_unit = self.width/self.x_range
    self.y_unit = self.hight/self.y_range

    x_scaled = (x-self.x_min)*self.x_unit+self.left
    y_scaled = (y-self.y_min)*self.y_unit

    return (x_scaled, self.bottom-y_scaled)

def coords_reversed(self, x, y):
    '''Convertes pygame coordinates into grid coordinates.'''  
    self.x_unit_rev = self.x_range/self.width
    self.y_unit_rev = self.y_range/self.hight

    x_scaled = (x-self.left)*self.x_unit_rev+self.x_min
    y_scaled = (y-self.top)*self.y_unit_rev

    return (x_scaled, self.y_scaled)
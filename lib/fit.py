def fit(self, scaling_factor: float=0.8):
        '''Scales the plot by the given factor.'''
        self.scaling_factor = scaling_factor
        self.top = self.given_top-(1-self.scaling_factor)/2*self.given_hight
        self.bottom = self.given_bottom-(1-self.scaling_factor)/2*self.given_hight
        self.left = self.given_left+(1-self.scaling_factor)/2*self.given_width
        self.right = self.given_right-(1-self.scaling_factor)/2*self.given_width
        self.hight = self.given_hight*self.scaling_factor
        self.width = self.given_width*self.scaling_factor
import numpy as np
class Match():
    def __init__(self,girl,boy):
        self.girl = girl
        self.boy = boy
        self.probability = 1.0 / np.math.factorial(10)
    
    def identifier(self):
        return self.girl + ":" + self.boy
    
    
import numpy as np


class Question:
  def __init__(self, difficulty, concept):
    self.d = difficulty
    self.c = concept
  
  def pRight(self, skill):
    return 1.0/(1.0 + np.exp(self.d - skill))
    

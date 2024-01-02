  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
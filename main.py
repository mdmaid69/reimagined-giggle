  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
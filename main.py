  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
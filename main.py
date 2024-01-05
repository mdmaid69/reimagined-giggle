  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
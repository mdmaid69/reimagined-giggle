  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
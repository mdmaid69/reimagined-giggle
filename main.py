  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
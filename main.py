def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
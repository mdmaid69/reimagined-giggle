def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
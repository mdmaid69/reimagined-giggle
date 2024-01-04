def count_words(sentence):
        return len(sentence.split())
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
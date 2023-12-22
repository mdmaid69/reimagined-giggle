  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def count_characters(sentence):
        return len(sentence)
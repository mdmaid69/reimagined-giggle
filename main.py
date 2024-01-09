  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
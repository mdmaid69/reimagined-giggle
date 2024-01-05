def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
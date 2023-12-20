def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
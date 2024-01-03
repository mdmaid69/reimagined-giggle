  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def count_words(sentence):
        return len(sentence.split())
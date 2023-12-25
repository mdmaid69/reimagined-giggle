  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def find_unique_words(sentence):
        return set(sentence.split())
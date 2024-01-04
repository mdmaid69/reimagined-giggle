def count_words(sentence):
        return len(sentence.split())
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
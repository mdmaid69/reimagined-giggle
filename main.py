  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
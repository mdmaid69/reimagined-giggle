  import os
  def split_path(path):
        return os.path.split(path)
def find_unique_words(sentence):
        return set(sentence.split())
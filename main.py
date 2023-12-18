  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def find_unique_words(sentence):
        return set(sentence.split())
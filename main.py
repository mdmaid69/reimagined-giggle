  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
def find_unique_words(sentence):
        return set(sentence.split())
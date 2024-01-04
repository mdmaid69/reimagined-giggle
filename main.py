  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def find_unique_words(sentence):
        return set(sentence.split())
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def count_words(sentence):
        return len(sentence.split())
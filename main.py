  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def find_unique_words(sentence):
        return set(sentence.split())
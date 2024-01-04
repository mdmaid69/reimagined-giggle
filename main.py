  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def count_words(sentence):
        return len(sentence.split())
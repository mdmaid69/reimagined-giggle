  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def find_unique_words(sentence):
        return set(sentence.split())
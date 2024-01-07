  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def find_unique_words(sentence):
        return set(sentence.split())
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
def find_unique_words(sentence):
        return set(sentence.split())
  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def find_unique_words(sentence):
        return set(sentence.split())
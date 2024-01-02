  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
def find_unique_words(sentence):
        return set(sentence.split())
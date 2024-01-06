  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
def find_unique_words(sentence):
        return set(sentence.split())
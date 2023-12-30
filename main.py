  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
def count_characters(sentence):
        return len(sentence)
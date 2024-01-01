  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
def count_words(sentence):
        return len(sentence.split())
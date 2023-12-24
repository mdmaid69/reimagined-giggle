def count_words(sentence):
        return len(sentence.split())
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
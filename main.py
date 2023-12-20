  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
def find_unique_words(sentence):
        return set(sentence.split())
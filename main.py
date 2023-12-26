  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def count_words(sentence):
        return len(sentence.split())
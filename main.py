  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def count_words(sentence):
        return len(sentence.split())
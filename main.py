  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
def count_words(sentence):
        return len(sentence.split())
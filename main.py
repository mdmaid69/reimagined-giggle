  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def find_unique_words(sentence):
        return set(sentence.split())
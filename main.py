  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def count_characters(sentence):
        return len(sentence)
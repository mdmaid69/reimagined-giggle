  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def count_characters(sentence):
        return len(sentence)
  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def count_words(sentence):
        return len(sentence.split())
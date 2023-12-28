  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def find_unique_words(sentence):
        return set(sentence.split())
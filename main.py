  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
def find_unique_words(sentence):
        return set(sentence.split())
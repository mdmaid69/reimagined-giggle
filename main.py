  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
def count_words(sentence):
        return len(sentence.split())
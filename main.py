  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def find_unique_words(sentence):
        return set(sentence.split())
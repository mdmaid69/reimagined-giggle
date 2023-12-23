  import os
  def delete_file(file_name):
        os.remove(file_name)
def find_unique_words(sentence):
        return set(sentence.split())
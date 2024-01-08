  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def find_unique_words(sentence):
        return set(sentence.split())
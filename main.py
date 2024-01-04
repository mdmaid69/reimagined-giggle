  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def count_words(sentence):
        return len(sentence.split())
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def count_words(sentence):
        return len(sentence.split())
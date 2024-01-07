  import os
  def delete_file(file_name):
        os.remove(file_name)
def count_words(sentence):
        return len(sentence.split())
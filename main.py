def count_words(sentence):
        return len(sentence.split())
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
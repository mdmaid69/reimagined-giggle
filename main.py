  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def find_unique_words(sentence):
        return set(sentence.split())
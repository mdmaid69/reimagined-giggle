  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def find_unique_words(sentence):
        return set(sentence.split())
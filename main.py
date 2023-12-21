  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
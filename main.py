  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
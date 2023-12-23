text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
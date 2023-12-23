text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
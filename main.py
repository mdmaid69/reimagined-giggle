text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def get_current_working_directory():
        return os.getcwd()
  import os
  def get_current_directory():
        return os.getcwd()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
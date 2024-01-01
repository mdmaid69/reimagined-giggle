text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def delete_file(file_name):
        os.remove(file_name)
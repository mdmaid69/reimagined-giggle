  import os
  def delete_file(file_name):
        os.remove(file_name)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
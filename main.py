  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
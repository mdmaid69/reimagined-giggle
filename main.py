import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
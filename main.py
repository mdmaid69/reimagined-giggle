text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
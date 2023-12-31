import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
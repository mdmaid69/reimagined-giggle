import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
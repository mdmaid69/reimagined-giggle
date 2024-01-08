import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def find_unique_words(sentence):
        return set(sentence.split())
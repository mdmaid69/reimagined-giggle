import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def find_unique_words(sentence):
        return set(sentence.split())
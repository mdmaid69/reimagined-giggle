import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def count_words(sentence):
        return len(sentence.split())
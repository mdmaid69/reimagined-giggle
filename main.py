import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def count_characters(sentence):
        return len(sentence)
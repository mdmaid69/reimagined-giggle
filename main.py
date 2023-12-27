import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def count_words(sentence):
        return len(sentence.split())
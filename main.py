import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
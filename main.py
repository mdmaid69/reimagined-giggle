def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
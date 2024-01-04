def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import shutil
def delete_directory(path):
        shutil.rmtree(path)
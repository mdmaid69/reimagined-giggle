import shutil
def delete_directory(path):
        shutil.rmtree(path)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import shutil
def delete_directory(path):
        shutil.rmtree(path)
def find_unique_words(sentence):
        return set(sentence.split())
import shutil
def delete_directory(path):
        shutil.rmtree(path)
def count_words(sentence):
        return len(sentence.split())
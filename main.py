import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def find_unique_words(sentence):
        return set(sentence.split())
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def count_words(sentence):
        return len(sentence.split())
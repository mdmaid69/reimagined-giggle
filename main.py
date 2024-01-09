import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def find_unique_words(sentence):
        return set(sentence.split())
import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def count_words(sentence):
        return len(sentence.split())
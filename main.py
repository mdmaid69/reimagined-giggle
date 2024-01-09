import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
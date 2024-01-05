def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import shutil
def move_file(src, dst):
        shutil.move(src, dst)
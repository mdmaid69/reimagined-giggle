def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
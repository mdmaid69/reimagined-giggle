import glob
def find_files(pattern):
        return glob.glob(pattern)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
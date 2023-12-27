import glob
def find_files(pattern):
        return glob.glob(pattern)
def find_unique_words(sentence):
        return set(sentence.split())
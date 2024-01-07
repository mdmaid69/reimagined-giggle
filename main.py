import glob
def find_files(pattern):
        return glob.glob(pattern)
def count_words(sentence):
        return len(sentence.split())
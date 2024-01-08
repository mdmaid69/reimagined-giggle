sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import glob
def find_files(pattern):
        return glob.glob(pattern)
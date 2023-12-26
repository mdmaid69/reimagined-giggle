sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
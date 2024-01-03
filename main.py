sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
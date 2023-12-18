import re
def split_string(pattern, string):
        return re.split(pattern, string)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
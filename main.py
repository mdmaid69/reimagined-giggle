import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
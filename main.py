import sys
def add_to_python_path(path):
        sys.path.append(path)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
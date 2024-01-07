import collections
def create_queue():
        return collections.deque()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
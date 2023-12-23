import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
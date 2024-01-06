def find_union(list1, list2):
        return set(list1) | set(list2)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
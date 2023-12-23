sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
def find_difference(list1, list2):
        return set(list1) - set(list2)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
def find_common_elements(list1, list2):
        return set(list1) & set(list2)
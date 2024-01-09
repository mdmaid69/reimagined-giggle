def find_unique_words(sentence):
        return set(sentence.split())
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
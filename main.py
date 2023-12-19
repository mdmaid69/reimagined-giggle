list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
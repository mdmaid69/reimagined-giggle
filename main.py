import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
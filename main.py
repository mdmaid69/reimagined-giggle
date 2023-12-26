list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import itertools
print(list(itertools.permutations([1, 2, 3])))
def find_difference(list1, list2):
        return set(list1) - set(list2)
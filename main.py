import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
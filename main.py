list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
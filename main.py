list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
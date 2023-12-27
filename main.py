import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
for i in range(5):
        print(i)
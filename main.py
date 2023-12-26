import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
i = 0
while i < 5:
        print(i)
        i += 1
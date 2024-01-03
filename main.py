import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
name = "Python"
print("Hello,", name)
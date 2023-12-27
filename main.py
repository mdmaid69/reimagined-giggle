text = "Hello, world!"
print("Words:", len(text.split()))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
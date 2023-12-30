import re
print(re.match("h.*o", "hello world"))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
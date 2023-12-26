import re
print(re.match("h.*o", "hello world"))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
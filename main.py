import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import re
print(re.match("h.*o", "hello world"))
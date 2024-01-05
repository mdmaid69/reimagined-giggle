import re
print(re.match("h.*o", "hello world"))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
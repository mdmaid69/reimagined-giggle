import re
print(re.match("h.*o", "hello world"))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
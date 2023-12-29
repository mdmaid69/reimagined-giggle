import re
print(re.match("h.*o", "hello world"))
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
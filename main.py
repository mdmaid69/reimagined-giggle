import os
print(os.getcwd())
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
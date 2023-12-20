text = "Hello, world!"
print("Words:", len(text.split()))
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
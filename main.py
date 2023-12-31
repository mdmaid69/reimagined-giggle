text = "Hello, world!"
print("Words:", len(text.split()))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
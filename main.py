text = "Hello, world!"
print("Reversed:", text[::-1])
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
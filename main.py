import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
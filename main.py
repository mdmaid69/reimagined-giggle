import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
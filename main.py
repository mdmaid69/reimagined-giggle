import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
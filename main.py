import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
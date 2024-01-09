import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
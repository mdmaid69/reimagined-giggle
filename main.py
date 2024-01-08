import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import glob
def find_files(pattern):
        return glob.glob(pattern)
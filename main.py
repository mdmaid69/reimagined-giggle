import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
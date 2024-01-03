import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
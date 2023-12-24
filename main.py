import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
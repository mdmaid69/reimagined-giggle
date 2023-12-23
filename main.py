  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
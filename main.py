import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
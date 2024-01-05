import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
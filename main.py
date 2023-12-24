def calculate_roi(gain, cost):
        return (gain - cost) / cost
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
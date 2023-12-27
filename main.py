def calculate_perpetuity(payment, rate):
        return payment / rate
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
def calculate_energy(mass, c=3*10**8):
        return mass * c**2
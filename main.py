import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
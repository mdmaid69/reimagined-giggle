import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import random
def roll_die():
        return random.randint(1, 6)
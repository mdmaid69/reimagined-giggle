import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import random
def generate_random_sample(population, k):
        return random.sample(population, k)
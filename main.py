import random
def generate_random_choice(choices):
        return random.choice(choices)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
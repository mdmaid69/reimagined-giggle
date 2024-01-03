import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
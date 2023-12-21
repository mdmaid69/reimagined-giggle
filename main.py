def calculate_volume(length, width, height):
        return length * width * height
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
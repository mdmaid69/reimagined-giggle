def find_difference(list1, list2):
        return set(list1) - set(list2)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
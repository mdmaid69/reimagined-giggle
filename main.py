import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def count_words(sentence):
        return len(sentence.split())
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
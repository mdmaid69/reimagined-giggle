import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
def find_unique_words(sentence):
        return set(sentence.split())
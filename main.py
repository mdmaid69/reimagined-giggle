import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
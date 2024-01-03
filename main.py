  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import sys
def exit_program():
        sys.exit()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
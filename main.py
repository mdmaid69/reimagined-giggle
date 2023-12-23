import sys
def exit_program():
        sys.exit()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
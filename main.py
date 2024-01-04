import sys
def exit_program():
        sys.exit()
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
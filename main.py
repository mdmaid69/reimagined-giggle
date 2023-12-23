  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
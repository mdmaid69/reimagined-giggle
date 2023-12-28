def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
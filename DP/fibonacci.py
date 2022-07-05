"""
the idea of dynamic programming

more optimized recursive approaches
store answers for the problems that were already solved before
"""
def fib(self, n: int) -> int:
    return self.fibMemoization(n, {})
    
def fibMemoization(self, n: int, memo: dict) -> int:
    if n < 2:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = self.fibMemoization(n - 1, memo) + self.fibMemoization(n - 2, memo)

        return memo[n]

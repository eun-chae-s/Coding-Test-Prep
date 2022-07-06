"""
Approach 1: Memoization
"""
def climbStairs(self, n: int) -> int:
    return self.climbStairsDP(n, {})
        
def climbStairsDP(self, n: int, memo: dict) -> int:
    if n <= 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = self.climbStairsDP(n - 1, memo) + self.climbStairsDP(n - 2, memo)
        return memo[n]

"""
Approach 2: Fibonacci

n = 1 => 1 way
n = 2 => 2 ways
n = 3 => 3 ways
n = 4 => 5 ways (n = 2 + n = 3)
n = 5 => 8 ways (n = 3 + n = 4)
"""
def climbStairs2(self, n: int) -> int:
  if n <= 2:
      return n
  values = [-1 for _ in range(n)]
  values[0] = 1
  values[1] = 2

  for i in range(2, n):
      values[i] = values[i - 1] + values[i - 2]

  return values[-1]

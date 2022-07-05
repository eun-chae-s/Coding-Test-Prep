"""
Approach 1: Use additional space (storage; hash map)
"""
def tribonacci(self, n: int) -> int:
    return self.triboDP(n, {})
    
def triboDP(self, n: int, memo: dict) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = self.triboDP(n - 1, memo) + self.triboDP(n - 2, memo) + self.triboDP(n - 3, memo)

        return memo[n]

"""
Approach 2: Use three variables that store the numbers
"""
def tribonacci2(self, n: int) -> int:
  if n == 0:
      return 0
  elif n == 1 or n == 2:
      return 1

  a, b, c = 0, 1, 1
  for _ in range(3, n):
      a, b, c = b, c, a + b + c

  return a + b + c

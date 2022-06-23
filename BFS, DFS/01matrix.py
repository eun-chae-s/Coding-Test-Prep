"""
My initial approach on Leetcode #542. 01 Matrix

Only 21/50 test cases passed:(

Used Breath-First Search algorithm
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        queue = [(0,0)]
        p1 = 0
        num = len(mat) * len(mat[0])
        unfilled = []
        
        while p1 < num:
            last = queue[p1]
            row, col = last[0], last[1]
            neighbors = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]

            if mat[row][col] == 0:
                result[row][col] = 0
            else:
                neighbors_original = [mat[r][c] for (r, c) in neighbors if len(mat) > r >= 0 and len(mat[0]) > c >= 0]
                
                if min(neighbors_original) == 0:
                    result[row][col] = 1
                else:
                    neighbors_values = [result[r][c] for (r, c) in neighbors if len(mat) > r >= 0 and len(mat[0]) > c >= 0 and result[r][c] > -1]

                    if neighbors_values == []:
                        result[row][col] = -2
                        unfilled.append((row, col))
                    else:
                        minimum = min(neighbors_values)
                        result[row][col] = minimum + 1
            
            for n in neighbors:
                if len(mat) > n[0] >= 0 and len(mat[0]) > n[1] >= 0:
                    if result[n[0]][n[1]] == -1:
                        result[n[0]][n[1]] = -2
                        queue.append((n[0], n[1]))
            
            p1 += 1
        
        for i in range(len(unfilled) - 1, -1, -1):
            item = unfilled[i]
            row, col = item[0], item[1]
            neighbors = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
            minimum = min([result[r][c] for (r, c) in neighbors if len(mat) > r >= 0 and len(mat[0]) > c >= 0 and result[r][c] > -1])
            result[row][col] = minimum + 1
        
        return result
        

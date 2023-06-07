'''
给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。

如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。

注意：可能存在元素相同的行，对应某一列相等，应该分别计数一次
'''
from collections import Counter
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        res, n = 0, len(grid)
        cnt = Counter(tuple(row) for row in grid)
        res = 0

        for j in range(n):
            res += cnt[tuple(grid[i][j] for i in range(n))]

# 注意：查找字典中不存在的key时返回0
# 时间复杂度：O(N2),将行放入哈希表中消耗O(n2) 读所有列的哈希表也消耗 O(n2)
# 空间复杂度：O(N2),哈希表的空间复杂度就是O(n2)


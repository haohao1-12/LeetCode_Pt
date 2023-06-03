'''
给你一个整数数组 gifts ，表示各堆礼物的数量。每一秒，你需要执行以下操作：

选择礼物数量最多的那一堆。
如果不止一堆都符合礼物数量最多，从中选择任一堆即可。
选中的那一堆留下平方根数量的礼物（向下取整），取走其他的礼物。
返回在 k 秒后剩下的礼物数量。

'''
# 最大堆法
from heapq import *
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        heapify(gifts) # 将序列改变为最大堆结构
        while k and -gifts[0] > 1:
            heapreplace(gifts, -math.isqrt(-gifts[0]))
            k -= 1
        return -sum(gifts)
    
'''
[25,64,9,4,100] --> [-25,-64,-9,-4,-100]
--> [-100,-64,-25,-4,-9] --> [-64,-9,-25,-10]
思路就是将元素取反，使用最大堆，heapreplace删除最小元素（pop）然后再插入目标元素
使用最大堆的原因是每次要删除最大元素，插入最大元素的平方根
'''
    
# 递归法

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """

        
        if k == 0:
            return sum(gifts)
        else:
            i = gifts.index(max(gifts))
            gifts[i] = int(math.sqrt(max(gifts)))
            return self.pickGifts(gifts, k-1)


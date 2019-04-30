# 1 
class Solution:
    def two_sum(self, nums, target):
        '''
        :nums: List[int]
        :target: int
        :return: List[int]
        '''
        d = {}
        size = 0
        while size < len(nums):
            if target - nums[size] in d:
                if d[target - nums[size]] < size:
                    return [d[target - nums[size]], size]
            else :
                d[nums[size]] = size
            size = size + 1

# 2
from typing import List 
# 用于类型检查，防止运行时出现参数与返回值不符合
def two_sum(nums: List[int], target:int) -> List[int]:
    s = {}
    for i, n in enumerate(nums):
        if (target - n) in s :
            return [s[target - n], i]
        else:
            s[n] = i

if __name__ == "__main__":
    #solu = Solution()
    num = [2, 7, 2, 11, 15]
    target = 9
    nums = two_sum(num, target)
    #nums = solu.two_sum(num, target)
    print(nums)
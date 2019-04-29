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

if __name__ == "__main__":
    solu = Solution()
    num = [2, 7, 2, 11, 15]
    target = 9
    nums = solu.two_sum(num, target)
    print(nums)
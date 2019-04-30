def even_list(nums):
    return [i for i in nums if i%2 == 0 and
    nums.index(i)%2 == 0]

if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7,8,9,10]
    print(even_list(nums))
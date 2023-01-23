# 59, 90, 96, 12, 28, 34, 88, 13, 48, 77
def sort(nums):
    if len(nums)>1:
        left_nums = nums[:len(nums)//2]
        right_nums = nums[len(nums)//2:]

nums = [59, 90, 96, 12, 28, 34, 88, 13, 48, 77]
sort(nums)

print(nums)
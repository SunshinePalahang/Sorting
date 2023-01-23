# 59, 90, 96, 12, 28, 34, 88, 13, 48, 77
def sort(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)
        sort(nums, left, partition_pos - 1)
        sort(nums, partition_pos + 1, right)

def partition(nums, left, right):
    i = left
    j = right
    pivot = nums[right]
    

nums = [59, 90, 96, 12, 28, 34, 88, 13, 48, 77]
sort(nums)

print(nums)
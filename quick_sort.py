# 59, 90, 96, 12, 28, 34, 88, 13, 48, 77
def sort(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)


nums = [59, 90, 96, 12, 28, 34, 88, 13, 48, 77]
sort(nums)

print(nums)
# 59, 90, 96, 12, 28, 34, 88, 13, 48, 77

def sort(nums):
    for i in range(9):
        min = i
        for j in range (i,10):
            if nums[j] < nums[min]:
                min = j

nums = [59, 90, 96, 12, 28, 34, 88, 13, 48, 77]
sort(nums)

print (nums)
# 59, 90, 96, 12, 28, 34, 88, 13, 48, 77

def sort(nums):
    for i in range(9):
        min = i
        for j in range (i,10):
            if nums[j] < nums[min]:
                min = j

        temp = nums[i]
        nums[i] = nums[min]
        nums[min] = temp


nums = [59, 90, 96, 12, 28, 34, 88, 13, 48, 77]
sort(nums)

print (nums)
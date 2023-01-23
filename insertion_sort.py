# 59, 90, 96, 12, 28, 34, 88, 13, 48, 77
def sort(nums):
    for index in range(1, len(nums)):
        min = nums[index]
        i = index - 1
        while i >= 0:
            if min < nums[i]:
                nums[i+1] = nums[i]
                nums[i] = min
                i = i - 1
            
            else:
                break
        print(nums)

nums = [59, 90, 96, 12, 28, 34, 88, 13, 48, 77]
sort(nums)

print(nums)
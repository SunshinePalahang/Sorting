# 59, 90, 96, 12, 28, 34, 88, 13, 48, 77

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j+1] = temp

                print(nums)


nums = [59, 90, 96, 12, 28, 34, 88, 13, 48, 77]
sort(nums)

print(nums)
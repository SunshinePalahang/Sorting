# 59, 90, 96, 12, 28, 34, 88, 13, 48, 77
def sort(nums):
    if len(nums)>1:
        left_nums = nums[:len(nums)//2]
        right_nums = nums[len(nums)//2:]

        sort(left_nums)
        sort(right_nums)

        i = 0
        j = 0
        k = 0
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[i]:
                nums[k] = left_nums[i]
                i += 1
                k += 1
            else:
                nums[k] = right_nums[j]
                j += 1
                k += 1

        while i < len(left_nums):
            nums[k] = left_nums[i]
            i += 1
            k += 1

        while j < len(right_nums):
            nums[k] = right_nums[j]
            j += 1
            k += 1

        print(nums)

nums = [59, 90, 96, 12, 28, 34, 88, 13, 48, 77]
sort(nums)

print(nums)
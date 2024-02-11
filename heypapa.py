print("hello mir manera krutit mir")

def ss(nums):
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
print(ss([1,3,1]))
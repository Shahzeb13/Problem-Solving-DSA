from typing import list
class solution:
def containsDuplicate(self, nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1 ,len(nums)):
            if nums[j] == nums[i]:
                return True
    return False

result = containsDuplicate([1 , 3 , 2 , 2])
print(result)

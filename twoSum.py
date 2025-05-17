def twoSum(nums , target):
    for i ,num in enumerate(nums):
        for j , num2 in enumerate(nums):
            if i != j and num + num2 == target:
                return i,j


res= twoSum([2 , 5 , 7, 6], 7) 

print(res)

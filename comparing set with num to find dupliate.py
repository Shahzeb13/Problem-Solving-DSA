

def containsDuplicate(nums):
    
    seen = set(nums);
    
    return len(seen) < len(nums);





res = containsDuplicate([2 , 3, 1 , 4 ,4])
res2 =  containsDuplicate([2 , 3, 1 , 4 ,5 , 8])
print(f" Has Duplicate : {res}");
print(f" Has Duplicate : {res2}");

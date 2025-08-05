

def containsDuplicate(nums):
    seen = set();
     
    for num in nums:
        if num in seen:
            print(f"Num ; {num}");
            print(f"Seen : {seen}");
            return True;
        seen.add(num);

    return False;




res = containsDuplicate([2 , 3, 1 , 4 ,4])
res2 =  containsDuplicate([2 , 3, 1 , 4 ,5])
print(f" Has Duplicate : {res}");
print(f" Has Duplicate : {res2}");

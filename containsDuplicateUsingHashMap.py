

def containsDuplicate(nums):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num , 0);
    print(f"Count : {count}");

    for key in count.keys():
        if count[key] > 1:
            return True;
    return False;




res = containsDuplicate([1 , 2, 3 , 4 ,4])
print(f" Has Duplicate : {res}");

 def test(nums , k):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num , 0)
  

    arr = []
    for num , count in count.items():
        arr.append([count , num])
    print(f"Array : {arr}")
    arr.sort()
    print(f"After Sorting : {arr}")
    res = []
    for _ in range(k):
        res.append(arr.pop()[1]);
    return f"Top K frequrent ELements : {res}"

result = test([1,2,2,2,2,3,3,3,4,4,4] , 3);
print(result)

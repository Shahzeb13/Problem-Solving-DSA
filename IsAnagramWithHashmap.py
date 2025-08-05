


def isAnagram(s , t):
    
    hashMapS = {}
    hashMapt = {}
    for num in s:
        hashMapS[num] = 1 + hashMapS.get(num , 0);
    for num in t:
        hashMapt[num] = 1 + hashMapt.get(num , 0)
    
    return hashMapS == hashMapt





res = isAnagram('racecar' , 'carrace')
print(res)

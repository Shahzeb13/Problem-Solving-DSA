def Lcp(strs):
    low = 0;
    high = len(strs) - 1;
    index = 0;
    prefix = "";
    while high >= low:
        if low == high:
            prefix += refChar;
            low = 0;
            index += 1;
        refChar = strs[high][index];
        word  = strs[low];

        if index >= len(word) or word[index] != refChar:
            return prefix;
        else: 
            low +=1;
    return prefix;





res1 = Lcp(["flower","flow","flight"])
res2= Lcp(["dog", "racecar", "car"])
print(f"Prefix : {res1}")

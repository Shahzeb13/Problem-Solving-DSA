def Lcp(strs):
    if not strs:
        return "";
    prefix = strs[0];

    for word in strs:
        while not word.startswith(prefix):
            prefix = prefix[:-1];
            if not prefix:
                return ""
    return prefix;





res1 = Lcp(["flower","flow","flight"])
res2= Lcp(["dog", "racecar", "car"])
print(f"Prefix : {res1}")

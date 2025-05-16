def isAnagram(string1  , string2):
    freq1 = {};
    freq2 = {};


    for char in string1:
        if char in freq1:
            freq1[char] += 1;

        else: 
            freq1[char] = 1


    for char in string2:
        if char in freq2:
            freq2[char] += 1;

        else: 
            freq2[char] = 1


    if freq1 == freq2:
        return True
    else:
        return False

res = isAnagram('bbcc' , 'ccbc')


print(res);

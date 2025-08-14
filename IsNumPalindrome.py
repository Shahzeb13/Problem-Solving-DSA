def IsNumPalindrome(x):
    strX = str(x);
    return strX=="".join(strX[::-1]);
    # return strX == reversedStrX;







output = IsNumPalindrome(10);
print(output);

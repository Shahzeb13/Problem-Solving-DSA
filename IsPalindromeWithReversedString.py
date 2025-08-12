def isPalindrome(str):
    #So, we have given a string and we gotta find if it is palindrome or not
    # At first I will try to use Two pointer approach, see if it works

    #Algorithm
    """
    create three variables i.ee low , high and index:
    set the first char as low and last as high!
    compare them in each iteraion, if they both matches continir the loop but if they do not break the loop and return false


    """
    #pseudocode
    """
    low = 0;
    high= len(str) - 1;
    inddex = 0;

    while high is greater than lwo:
        Compare high and low:
        if high and low mathces:
            move low to the next index
            move high to to prev index;
        else if the don't match:
            return fasle
    return true if all of them matches:



    """
    # filteredStrList= [c for c in str if c.isalnum()];
    # filteredStr = "".join(filteredStrList);
    # lowerFilteredStr = filteredStr.lower();
    # print(f"Lower Filtered String : {lowerFilteredStr}");
    # low = 0;
    # high= len(lowerFilteredStr) - 1;
    # index = 0;
    
    # while high >= low:
    #     print(f"================= Iteration {index}========================");
    #     if lowerFilteredStr[low] == lowerFilteredStr[high]:
    #         low = low + 1;
    #         high = high - 1;
    #         index += 1;
    #     else:
    #         index += 1;
    #         return False;
    # return True;



    newStr = "";
    for c in str:
        if c.isalnum():
            newStr += c.lower();
    return newStr == newStr[::-1];
    












# res = isPalindrome("tab a cat");
res = isPalindrome("Was it a car or a cat I saw?");
# Was it a car or a cat I saw?
print(res);

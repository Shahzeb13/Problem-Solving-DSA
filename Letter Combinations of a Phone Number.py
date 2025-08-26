from unittest import result


def LCOPN(digits):

    if not digits:
        return [];

    '''

    ===Problem===
    So, I will be given a digits array ["45] and i will have to return possible combinations of alphabets
    for those number just like they are printed on the keypaid phone.


    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


    AlphaNumMap = {
    "1" : "",
    "2" : "abc",
    "3" : "def",
    "4" : "ghi",
    "5" : "jkl",
    "6" : "mno",
    "7" : "pqrs",
    "8" : "tuv",
    "9" : "wxyz"

    }

    requiredNum = []
    for char in digits:
        if char in AlphaNumMap:
            requiredNum.append(AlphaNumMap[char]);

    so requiredNum will become ["abc" ,"def"]
    
    outputDigits = []
    for i in range(len(requiredNum[0])):
        for j in range(len(requiredNum[1])):
            res = i * j;
            outputDigits.append(res);

    return outputDigits;




    ===Dry Run===

    I






    How can i solve this problem?

    ===psudoCode===


    '''
    
    AlphaNumMap = {
    "1" : "",
    "2" : "abc",
    "3" : "def",
    "4" : "ghi",
    "5" : "jkl",
    "6" : "mno",
    "7" : "pqrs",
    "8" : "tuv",
    "9" : "wxyz"

    }

    # required = []
    # for char in digits:
    #     if char in AlphaNumMap:
    #         required.append(AlphaNumMap[char]);
    # print(required)
    # # so requiredNum will become ["abc" ,"def"]
    # outputDigits = []


    # if len(required) == 1:
    #     for char in required:
    #         outputDigits += char;
    #     return outputDigits;



    # # outputDigits = []
    # for i , val in enumerate(len(required) - 1):
    #     for j , val in enumerate( i + 1, len(required)):
    #         res = required[i] + required[j];
    #         outputDigits.append(res);

    # return outputDigits;

    #i was stuck at this part so I had to took help of AI and I understand the problem now



    required = []
    for char in digits:
        if char in AlphaNumMap:
            required.append(AlphaNumMap[char]);
    print(required)
    outputDigits = [""]

    for group in required:
        temp = [];
        for prefix in outputDigits:
            for char in group:
                temp.append(prefix + char);
        outputDigits = temp;
    return outputDigits;
    

    '''
    ===dryRun===
    iteration[out]    Iter[inner]    required               group      outputDigits         prefix          char     prefix + char      temp     

        0                  0      ['abc', 'jkl']           abc           [""]               ""               a          "" + a          ["a"]
        0                  1                                                                                 b           "" + b         ["a","b"]
        0                  2                                                                                 c           ""+ c          ["a","b","c"]
        now outputDigits= = ["a" ,"b" , "c"]

    iteration[out]    Iter[inner]    required               group      outputDigits         prefix          char     prefix + char      temp 
        1                  0                                 jkl      ["a" ,"b" , "c"]        "a"            j            "aj"          ["aj"]
        1                  1                                                                  "a"            k            "ak"          ["aj","ak"]
        1                  2                                                                   "a"            l            "al"         ["aj","ak,"al"]
        1                  0                                 jkl       ["aj","ak,"al"]         "b"            j           "bj"          ["aj","ak,"al","bj"]
        1                  1                                                                   "b"            k            "bk"         ["aj","ak,"al","bj","bk"]
        1                  2                                                                   "b"            l           "bl"          ["aj","ak,"al","bj","bk","bl"]
        same for the character c 
        

        if there are nested data strucutres like strings in array! and you want to access the nested data stucture
        element then use first loop to captures that ddata structure 
   '''



output = LCOPN("25")
print(output)

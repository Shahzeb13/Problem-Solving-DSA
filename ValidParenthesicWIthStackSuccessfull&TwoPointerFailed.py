def ValidParanthesis(s):
    print("=======================Valid Paranthesis===========================");
    '''
    "Pseudo Code"
    ([{}])
    
    low is 0
    high is len(s) - 1

    while high is greater than low:
        if s[low] == s[high]:
            low +=1;
            high -=1;
            continue;
        else:
            return false;
    return true;

    ===Dry Run===
    ([{}])
    Iteration   low     high         low[val]       high[val]          if condition

        0        0        5             (               )                   true
        1        1        4             [               ]                   true
        2        2        3             {               }                   true
    [(])
    Iteration   low     high         low[val]       high[val]          if condition
        0        0       3              [               )                   false

    '''
    #Implementation
    # low = 0
    # high = len(s) - 1

    # while high > low:
            
    #     if s[low] == s[high]:
    #         print("if statement triggered")
    #         low +=1;
    #         high -=1;
    #         continue;
    #     else:
    #         print("Else Statement Triggered")
    #         return False;
    # return True;


    '''

   Stack Attempt

    while stack:
        char = stack.pop();
        stack2.append(char);



    ===dry run===

    iteration       pop           char      PoppedStr      
        0            y             )         )
        1            y             ]         )]
        2            y             }         )]}
        3            y             {         )]}{
        4            y             [         )]}{[
        5            y             (         )]}{[(

        ([{}]) == )]}{[(




    ===problem===
    so i have to check that the bracket are opening and closing in the correct order
    ====psuedocode===
    parantthesicMap = {
        "]" : ["["],
        "}" : ["{"].
        "}" : ["{"]
    }

    [(])
    
        stack = ["[" , "("]
       


    openBracketsRule = ["[" , "{" , "("]
    closingBracketsRule = ["]" ,"}" ,")"]
    closeBrakets = []
    stack = [];
    for char in s:
        if char in openBracketsRule:
            put char in stack
        else:
            put char in closeBrackets
        
    ==hashmap===
    bracketMap ={closingBracets[i] : openingBrackets[i] for i in range(len(closingBracket))}
    bracketMap = {
        "]" : ["["],
        "}" : ["{"].
        ")" : ["("]
    }
    the above code is to put opening paranthesic in the stack
    for char in closingBrakets:
        if char is in bracketMap and and stack[-1] is in bracketMap[char]:
            stack.pop();
        return False:
    return True;

    """dry run""

    "([{}])"


    iteration   char            stack
        0         }      ["[" , "{" , "("]
        1         ]      ["[" , "("] 
        2         )      ["("]
        NO THIRD ITERATION
        STACK BECOMES ZER0

    "[(])"
    
    iteration   char            stack
        0         ]      ["[" , "("]
        terminates
        return fasle



    [(])
    ===dry run===
    for loop 1
    iteration   stack       closingBracket
        0        ["["]          []
        1        ["[","("]      []
        2        ["[","("]      ["]"]
        3        ["[","("]      ["]",")"]

    for loop 2

    Stack            closingBracket
["[","("]            ["]",")"]

bracketMap = {
        "]" : ["["],
        "}" : ["{"].
        ")" : ["("]
    }

    Iteration      Stack             closingBracket         char
        0          ["["]                ["]",")"]            ]
        loop terminates
        return False;

        



    '''


    # reversedS = s[::-1];
    # print(f"Reversed String : {reversedS}");
    # stack = [];
   
    # for char in s:
    #     stack.append(char);
    # PoppedStr ="";
    # while stack:
    #     PoppedStr += stack.pop();
    # print(f"PoppedStr : {PoppedStr}");
    # if reversedS == PoppedStr:
    #     return True;
    # else:
    #     return False;

    '''
    Stack  : ['(', '[', '{']
    CloseBracketsList : ['}', ']', ')']
    BucketMap : {']': '[', 
                '}': '{', 
                ')': '('
                }
    s = "([{}])"
    iteration       char       stack
        0             }       ['(', '[']
        1             ]       ['(']
        2             )         [] 


    "()[]{}"
    For loop 1 
    TIeration       char        stack       closeBracketsList
        0             (         ["("]
        1             )                         [")"]
        2             [         ["(","["] 
        3             ]                         [")","]"]
        4             {         ["(","[" ,"{"]  
        5             }                         [")","]","}"]


        Stack =   ["(","[" ,"{"]
        closeBracketsList      = [")","]","}"]
        BucketMap : {']': '[', 
                '}': '{', 
                ')': '('
                }
    for loop 2
    Iteration   char        stack
        0         )           {
        returns false      


    "()[]{}"
    
    '''


    # openingBracketsRule = ["[" , "{" , "("]
    # closingBracketsRule = ["]" , "}" , ")"]
    # closeBracketsList = []
    # stack = [];
    # for char in s:
    #     if char in openingBracketsRule:
    #         stack.append(char);
    #     else:
    #         closeBracketsList.append(char);
    # print(f"Stack  : {stack}")
    # print(f"CloseBracketsList : {closeBracketsList}")
    # print("\n")

    # #crarting bucketMap for rules

    # bucketMap = {closingBracketsRule[i] : openingBracketsRule[i] for i in range(len(closingBracketsRule))}
    # print(f"BucketMap : {bucketMap}")


    # for char in closeBracketsList:
    #     if char in bucketMap and stack[-1] in bucketMap[char]:
    #         # print("if Block entered..")
    #         stack.pop();
    #         continue;
    #         # print(f"stack after element is poped : {stack}")
    #     return False;
    # return True;



    openingBracketsRule = ["[" , "{" , "("]
    closingBracketsRule = ["]" , "}" , ")"]

    bracketMap = { closingBracketsRule[i] : openingBracketsRule[i] for i in range(len(closingBracketsRule))};

    stack = [];
    print(bracketMap)
    for char in s:
        if char in openingBracketsRule:
            stack.append(char);
        elif char in closingBracketsRule:
            if not stack or stack[-1] != bracketMap[char]:
                # print("Hey")
                return False;
            stack.pop();
    return len(stack) == 0;



            

      

   



# output = ValidParanthesis("([{}])");
output = ValidParanthesis("[(])");
# output = ValidParanthesis("()[]{}")
# "[(])"
print(output)

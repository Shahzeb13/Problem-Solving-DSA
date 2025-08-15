def RomanToInteger(s):

    # RomanList = ["I" , "V" , "X" , "L" , "C" , "D" , "M" ];
    '''
    if sorted in alphabetical order
    [C,D,I,L,M,V,X];
    if I with X and I with V
    if L with X and  with C
    c with D AND M
LCDM 

   RSRules = {
    "I": ["V", "X"],
    "X": ["L", "C"],
    "C": ["D", "M"]
    }


    values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}



    '''

    RSRules = {
    "I": ["V", "X"],
    "X": ["L", "C"],
    "C": ["D", "M"]
    }


    values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


    romanData = {

        "I" : { "value" : 1  , "subtracted_from" : ["V" , "X"]},
        "V" : { "value" : 5  , "subtracted_from" : []},
        "X" : { "value" : 10  , "subtracted_from" : ["L" , "C"]},
        "L" : { "value" : 50  , "subtracted_from" : []},
        "C" : { "value" : 100  , "subtracted_from" : ["D" , "M"]},
        "D" : { "value" : 500  , "subtracted_from" : []},
        "M" : { "value" : 1000  , "subtracted_from" : []},
    }
    
    if not s:
        return "";
    output = 0;
    i = 0;
    while i < len(s):
        current = s[i];
        print(f"======================Iteration {i}======================")
# MCMXCIV
        print(f"Current : {current}")

        
        next = s[i + 1] if i + 1 < len(s) else None;
        print(f"Next : {next}")
        if current in romanData and next in romanData[current]["subtracted_from"]:
            print(f"If block is true for {i}th Iteraion");
            print(f"Output Before Sum : {output}");
            output += romanData[next]['value'] -romanData[current]['value'];
            print(f"Output After Sum : {output}");
            print(f"{romanData[next]['value']} - {romanData[current]['value']}")
            i += 2;
            continue;
        print(f"Output Before Ssum : {output}");
        output += romanData[current]["value"];
        print(f"Output after Ssum : {output}");
        print(f"{output} + {romanData[current]['value']}")
        i += 1;

    return output;

    



    # for char in s:
    #     if char=="M":
    #         output += 1000;
    #     elif char == "D":
    #         output += 500;
    #     elif char == "C":
    #         output += 100;
    #     elif char == "L":
    #         output += 50;
    #     elif char == "X":
    #         output += 10;
    #     elif char == "V":
    #         output += 5;
    #     elif char == "I":
    #         output += 1;
    # return output;





output = RomanToInteger("M");
print(output);

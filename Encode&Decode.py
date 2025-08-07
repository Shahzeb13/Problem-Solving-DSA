def Encode(sentence):
    #algorithm to solve this problem
    #what do I neeed to achieve
    # I have to convert a list of strings to one string 
    #["I" , "Love" , "you" , "broski"] >>>[ I#Love#you#broski]
    #SOrting  , hashmap , hashset , twopointer, heap ,
     
    # hashMapStr = {};
    # str = ""
    


    if sentence == []:
        return "".join(sentence)
    if sentence == [""]:
        return "[""]";
    
        
    str = "#shahzeb@123".join(sentence)
    return str;
        

res = Encode(["we","say",":","yes","!@#$%^&*()"])
# res2 = Encode(["we","say",":","yes"])
# res3 = Encode([])
print(res)
# print(res2)
# print(f"Res : {res3}")
def Decode(str):
    # decodedArr = []
    # i = 0;
    # for word in arr:

    if str == "":
        return [];
    if str == "[""]":
        return [""]
    arru = str.split('#shahzeb@123');
    return arru

# Decode(res2);
response1 = Decode(res);
print(f"{response1}");
# response = Decode(res3);
# print(f"{response}")



# print("#".join([""]));




age = 19;
strAge = str(age);
# print(type(strAge))


def Encode(strs):
    if not strs:
        return "";

    sizes , res = [] , "";
    for s in strs:
        sizes.append(len(s));
    for sz in sizes:
        res += str(sz);
        res += ",";
    res += "#"
    # print(f"Res : {res}");
    for s in strs:
        res += s;
    print(f"Res : {res}")


Encode(["Neet" , "code" , "loves"  , "you"])



def Decode(s):

    if not s:
        return [];
    sizes , res , i = [] , [] , 0;
    while s[i] != '#':
        sStr = "";
        while s[i] != ",":
            sStr += s[i];
            i += 1;
        sizes.append(int(sStr));
        i += 1;
    i += 1;  # when the outer whole loop breaks i will become i + 1 to move to the inedx next to #
    for sz in sizes:
        res.append(s[i:i + sz]);
        i += sz;
    return res;

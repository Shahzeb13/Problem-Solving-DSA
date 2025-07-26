from collections import Counter;
def groupAnagram(strs):
    # ismatched = 0;
    # ["act","pots","tops","cat","stop","hat"]
    listOfAnagrams = []
    used = set()
    for i in range(len(strs)):
        if i in used:
            continue
        # ismatched = 0;


        print(f"---------------------- {i}th iteration----------------------")
        # print(f"ismatched is reset to zero for {i} iteration")
        
        group = [strs[i]];
        
        for j in range(i + 1 , len(strs)):
            if j in used: 
                continue
            if len(strs[i]) == len(strs[j]):
                isTrue =   Counter(strs[i]) == Counter(strs[j])#check the freq of the words
                if(isTrue):
                    print(f"{strs[i]} and {strs[j]} are anagrams")

                    # ismatched += 1;
                    print(f"Match found for {strs[i]} with {strs[j]}")
                    
                
                    group.append(strs[j])
                    used.add(j)
                    
                    # print(f"{listOfAnagrams} During {i}th Iteraion ")
                
                    # print(f"{group} is added to ListOfAnagrams")
                    continue;
                print(f"{strs[i]} and {strs[j]} are not anagrams")
                
                continue;
            print(f'Length of {strs[i]} is not equal to {strs[j]}')
            continue;


        listOfAnagrams.append(group);
        reversed = []
        for i in range(len(listOfAnagrams) - 1 , -1 , -1):
            reversed.append(listOfAnagrams[i]);

    return reversed;


res = groupAnagram(["act","pots","tops","cat","stop","hat"])
print(res)

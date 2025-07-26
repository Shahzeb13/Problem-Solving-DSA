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



//Explanation
Anagrams are the words that have same frequency and same length i.e. cat and act
Problem Statement:
We have to give a function an array of Anagrams and then we want that fucntion to return a list of lists i.e [[hat] , [tops , pots , stop] , [act , cat]]
Here is the algrothim for solving this problem.
1. First of all, I have to create an empty list to store the grouped anagrams
2. I have to use two loops to compare each anagram with its fellow neighbours.
3. I will also use set() to make sure that once a jth word is matched for the ith term! we will group them together to avoid using that same word comparision with another Word.
3. Simple we will iterate J+1th term for every ith term skipping those who are already used. AFter that we wiull return the list in reversed.



class MajElem:


    def __init__(self, nums):
        self.nums = nums;




    def findMajElem(self):
        '''
        I can try to use hashmap to store the element as the keys and count as values;
        then i can iterate over hashmap to check if the value a specific key is greater the halve len of the array



        '''
        
        hashCount = {};
        for num in self.nums:
            hashCount[num] = 1 + hashCount.get(num , 0);
        print(hashCount);
        
        for key in hashCount.keys():
            if hashCount[key] > len(self.nums) /2:
                return key;



def main():

    s = MajElem([2,2,2]);
    output = s.findMajElem();
    print(output);


if __name__ == "__main__":
    main();
                
        

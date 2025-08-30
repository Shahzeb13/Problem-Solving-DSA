class RemoveElement:
    
    def __init__(self , nums):
        self.nums = nums;


    def removeElement(self , val):
        if not self.nums:
            return len(self.nums);
        
        low = 0;
        high = len(self.nums)  - 1;
        i = 0;
        while high >= low:
            print(f"{i}th Iteration");
            # if high >= len(self.nums) -1 :
            #     high = len(self.nums) -1;


            # if len(self.nums) == 1:
            #     if self.nums[low] == val:
            #         self.nums.pop(low);
            #         break;
            if len(self.nums) == 1:
                if self.nums[low] == val:
                    self.nums.pop(low);
                    return 0;
                else:
                    return 1;

            if self.nums[low] == val:
                self.nums.pop(low);
                high = len(self.nums) -1;
            else:
                low +=1;
            
            if self.nums[high] == val:
                self.nums.pop(high);
                high = len(self.nums) -1;
            else:
                high -=1;
            i +=1
        return len(self.nums)

    '''

    ===dry run===
    itertion    low     high        low[val]        high[val]       pop

        0        0       4              1               4            1
        1        1       3              1               3            1


    ==dry run again===
         itertion    low     high        low[val]        high[val]       pop        list becomes

            0         0       4             1               4             1          [1,2,3,4]
            1         0       2             1               3             1          [2,3,4]
            2         0       0             2               2             none        [2,3,4]


    [0,1,2,2,3,0,4,2]
       

    '''





def main():
    re = RemoveElement([2]);
    print(re.removeElement(2))



if __name__ == "__main__":
    main();

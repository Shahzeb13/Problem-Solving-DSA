

class ContanateArray:


    def __init__(self, nums):
        self.nums = nums;




    def doArrayConcatenation(self):
        '''
        mayve i have to create a dynamic array with twice the size of the nums array.
        what if i iterate over nums and range funcion ! i multiply the range with 2! so that it
        will become the double the original array!


        arr = []'
        for i in range((len(nums) -1) * 2):
            arr.append(i);
            arr.append(i+4);
        
        print(arr);



        '''
        
        numsLength = len(self.nums);
        for i in range(numsLength):
            self.nums.append(self.nums[i]);
           
            
        
        print(self.nums);



def main():

    s = ContanateArray([1,2,3,4]);
    output = s.doArrayConcatenation();
    print(output);


if __name__ == "__main__":
    main();
                
        

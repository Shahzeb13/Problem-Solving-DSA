
from re import L


class BinarySearch:
    def __init__(self , nums):
        self.nums = nums;
        
    

    def ExecuteSearch(self , target):
        
        #Logic goes here
        low = 0;
        high = len(self.nums) -1;
        

        while high >= low:
            mid = (low + high) //2;

            if self.nums[mid] == target:
                return mid;
            if self.nums[mid] < target:
                low = mid + 1;
            else: 
                high = mid -1;

        return -1;

      




def main():

    s = BinarySearch([-1,0,2,4,6,8]);
    print(s.ExecuteSearch(4));





if __name__ == "__main__":
    main();

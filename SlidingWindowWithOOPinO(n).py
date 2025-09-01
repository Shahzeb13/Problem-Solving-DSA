class slidingWindow:
    def __init__(self , nums):
        self.nums = nums;





    def InititateSlidingWindow(self, k):

        windowSize = sum(self.nums[:k]);
        
        n = len(self.nums);
        maxSum = windowSize;


        for i in range(n -k):
            currentSum = windowSize - self.nums[i] + self.nums[i + k];
            maxSum = max(currentSum ,maxSum);
        return maxSum;
            


        '''
        ==dry run===
        [4,5,6,-1,0,4,5]
        iteration      i        firstWindowSum                currentWindowSum               maxSum


            0          0              15                             10                     15
            1          1              15                             5                      15
            2          2              15                            3                       15
            3          3              15                             9                      15
        
        '''



def main():
    s = slidingWindow([4,5,6,-1,0,4,5]);
    output = s.InititateSlidingWindow(3)
    print(output)






if __name__ == "__main__":
    main()
        

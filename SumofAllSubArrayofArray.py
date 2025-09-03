class SumofSubArray:

    def __init__(self , nums):
        self.nums = nums;
        self.totalSum = 0;




    def findSum(self):
        n = len(self.nums);
        for i in range(len(self.nums)):
            contribution = self.nums[i] * (i + 1) * (n - i);
            self.totalSum += contribution;

        return self.totalSum;




def main():
    s = SumofSubArray([2, 1, 3, 4]);
    output = s.findSum();
    print(f"Total COntributon : {output}");


if __name__ == "__main__":
    main(); 



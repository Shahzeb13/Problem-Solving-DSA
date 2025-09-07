from re import L


class BestTimeToBuyStock:


    def __init__(self, prices):
        self.prices = prices;
        self.maxProfit = 0;



    def findBestTime(self):
        #Naive approach/Brute Force
        '''
        time complexity is o(n2)
        spcce complexity is o(n)
        
        
        '''
        # if not self.prices:
        #     return "";
        # if len(self.prices) == 1:
        #     return 0;
        # for i in range(len(self.prices)):
        #     for j in range(i+1 , len(self.prices)):
            
        #         if self.prices[j] < self.prices[i]:
        #             continue;
        #         currentProfit = self.prices[j] - self.prices[i];
        #         self.profits.append(currentProfit);
        # print(f"Total Profits : {self.profits}");
        # return  0 if max(self.profits) <= 0  else  max(self.profits);
        '''
        In bruteforce,  you can skip the sum of those valeus where ith index value is greater than jth value cause that will result
        in minus value and we are only concerned about the profit casue it always positive value
        so i want the pointer to move the left pointer to the smallest values and move the right to the largest values

        [10,1,5,6,7,1] if val[left+1] < val[right-1]  : move right porinter : move left pointer    for left pointer i will moveit it if the 
        next value is smaller and move the right pointer if the next value is larger else if both are true move either of them

        iteraiton   i       j       val[i]          val[j]          diff
            0       0       5         10               1             -9
            1       1       5         1                1              0
            2       1       4         1                7              6
            3       2       7         5                7              2
            4       3       4         6                7              1

            largest 6


        [3,2,6,5,0,3]
        my appraoch right now if that I want smaller value onthe left side an larger on the right side to calculate the profit! 
        It means that I have to go though all the posiibilities where rightpoiinter value is larger than left pointer value
        iteraiton   i       j       val[i]          val[j]          diff
            0       0       5         3                3             0
            1       1       5         2                3             1
            2       2       5         6                3             -3
            3       3       5         5                3             2
            4       4       5         0                3             3


        '''
        # [10,1,5,6,7,1]
        # [5,1,5,6,7,1]
        # [3,2,6,5,0,3]
        
        # left = 0;
        # right = len(self.prices) -1;
        
        # while right > left:
        #     currentdif = self.prices[right] - self.prices[left];
        #     self.profits.append(currentdif);
        #     if not (self.prices[left + 1] < self.prices[left]) and not (self.prices[right - 1] > self.prices[right]):
        #         right -=1;
        #         left += 1;
        #     elif self.prices[left + 1] < self.prices[left]:
        #         left +=1;
        #     elif self.prices[right - 1] > self.prices[right]:
        #         right -= 1;
        # return 0 if max(self.profits) <= 0 else max(self.profits);

        # maxStock = max(self.prices);
        # print(maxStock);


        # for i in range(len(self.prices)):
        #     currProfit = maxStock - self.prices[i];
        #     self.profits.append(currProfit);
        # return max(self.profits);

        '''
            [3,2,6,5,0,3]
            Itr     i       j       val[i]          va[j]           currentdif          profits
            0       0       5          3              3                 0               [0]
            1       1       5          2              3                 1               [0,1]
            2       1       4          2              0                 -2              [0,1,-2]
            3       1       3          2              5                 3               [0,1,-2,3]
            4       1       2          2              6                 4               [0,1,-1,3,4]


            [2,1,2,1,0,1,2]
        Itr     i       j       val[i]          va[j]           currentdif          profits
            0      0       6         2               2                  0               [0]
            1      1       6         1               2                  1               [0,1]
            2      1       5         1               1                  0               [0,1,0]
            3      1       4         1               0                  -1              [0,1,0,-1]
            4      1       3         1               1                  0               [0,1,0,-1,0]
            5      1       2         1               2                  1               [0,1,0,-1,0,1]
            6      1       1 loop terminates


            [2,1,2,1,0,1,2]
        Itr     i       j       val[i]          va[j]           currentdif          profits
            0      1       6         2               2                  0               [0]
            1      1       6         1               2                  1               [0,1]
            2      2       5         2               1                  1               [0,1,1]
            3      3       5         1               1                  0               [0,1,1,0]
            4      4       5         0               1                  1               [0,1,1,0,1]
            5          loop terminates


        what if i move the right pointer only if there is a highter values to the right
        left pointer shoud be set at



        what if i use a right pointer to find the biggest sell value in the array and use left to calculate the profit



        note:
        Left pointer = candidate buy day.

        Right pointer = candidate sell day.

        Valid profit = prices[right] - prices[left] only if positive.

        So i need to find a way to calculate all the posibilites where right pointer values is greater than 
        let pointer values!???????

        [3,2,6,5,0,3]
        ===algrithm===
        declare a maxProfit valirable
        declare a minBuy varaible
        declare left pointer = 0  and save its values in minBuy varaible
        declare right pointer = 1l

        declare a while loop:
        compare the right and left pointer values
        calculate the difference between them
        maxProfit = prices[right] - prices[left]:

        if maxProfit is in negative shrink the window by movign the left pointer and saving the value in
        minBuy variable
        if maxProfits is smaller then the previous maxProfit vales do nothing!
        return the maxProfit value at the end!

        ===dry run===
        [3,2,6,5,0,3]
        itr     left       right      left[val]/minBuy          right[val]      maxProfit
        0         0          1              3                      2              2-3 = -1 increment left and right
        1         1          2              2                      6              6-2 = 4 increment right pointer
        2         1          3              2                      5              5 -2 = 3 max(4 , 3) = 4
        3         1          4              2                      0              0-2 = -2 increment left and right
        4         2          5              6                      3              3-6 = -3 incremnt left and right!
        but right pointer is reached the end so maxprofit is gonna b 4



        [10,8,7,5,2]
        itr     left       right      left[val]/minBuy          right[val]      maxProfit
        0        0           1              10                       8             8-10 = -2  increment left and rght pointer
        1        1           2              8                        7             7-8 - -1 max(-1 , -2 ) = -1 but negative so incremnt left/right
        2        2           3              7                        5              5-7 = -2 max(-1 , -2) = -1 increment left/right
        3        3           4              5                        2              2-5 =-3 max(-1 , -3) = -1 incremnt left/right
        right pointer has reached the end but wait! the maxprofit is negatvie so we will return negative



        ===psuedoCode===
        minBuy = 0;
        right = 1;
        # minBuy = prices[left];
        maxProfit = 0;
        while right < len(prices):
            currentProfit = prices[right] - prices[minBuy];
            

            if currentProfit < 0 :
                minBuy = right;
                right +=1
                continue;
            else:
                maxProfits = max(maxProfits ,currentProfit);
                right += 1;

        '''         
        if not self.prices:
            return 0;
        if len(self.prices) == 1:
            return 0;
        minBuy = 0;
        right = 1;
        # minBuy = prices[left];
        
        while right < len(self.prices):
            currentProfit = self.prices[right] - self.prices[minBuy];
            

            if currentProfit < 0 :
                minBuy = right;
                right +=1
                continue;
            else:
                self.maxProfit = max(self.maxProfit ,currentProfit);
                right += 1;
        return self.maxProfit;



def main():
    s = BestTimeToBuyStock( [3,2,6,5,0,3]);
    maximumProfit = s.findBestTime();
    print(f"Maximum Profit : {maximumProfit}");


if __name__ == "__main__":
    main();

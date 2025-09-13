import math
from re import L

class KokoLovesBananas:


    def __init__(self, piles, h):
        self.piles = piles;
        self.h = h;
        self.speedList = [];

'''
In this brute force method, I tried to simulate koku eating minimum number of bananas she can eat to eat all the piles in the given number of hours,
the ith loop act as the speed that koku can choose to eat like how many banans she can eat per hours to completely eat all the pules in the given time frame.
the jth loop act as the piles of banans like for each pile we are calculateing the hours koku take for a specific speed!
the kth loop act as koku actually eating bananas! so each time koku eat n bananas from piles at n speed! we subtract the amount fromt he totalBananas!
if the total banans for that specific piles becomes negative or zero! we simply break the loop as to move koku to anohter pile and do the same for that pile.
For each time jth loop end we calculate if the hoursTaken are smaller then the given time frame h! if it is we return it!
Now the question arises that how that condition give the minumum spped! 
Answer lies in the iterioan of ith loop as we can see that we are testing speeds form small to large so the first speed that satisifies the condition is actually the minum speed koku can eat
bannas and complete the task in h time frame!


this method is purely brute force! i will try to solve it with some optimized technique or pattern!

I hope the explanation helped!

I did not performed any dry run or psuedocode because i did them on hard copy as that is very convenient for me! 




'''

    def findBestSpeed(self):
        #Naive approach/Brute Force
        for i in range(1 ,  max(self.piles) + 1):
            hoursTaken = 0;
            for j in range(len(self.piles)):
                remBan = self.piles[j];
                for k in range(self.piles[j]):
                    remBan = remBan - i;
                    hoursTaken += 1;
                    if remBan <= 0:
                        remBan = 0;
                        break;
                    # if remainingBananas == 0:
                    #     continue;
                    
                    # if hoursTaken > self.h:
                    #     hoursTaken = 0;
                    #     continue;
            
            if hoursTaken <= self.h:
                return i;
       
            
    

    
       


def main():
    s = KokoLovesBananas([25,10,23,4],4);
    maximumProfit = s.findBestSpeed();
    print(f"Minummum speed needed to eat all bananans : {maximumProfit}");


if __name__ == "__main__":
    main();

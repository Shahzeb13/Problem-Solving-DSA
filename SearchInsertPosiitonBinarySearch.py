
I solved this directly in leetcode Instead of IDE so it llooks different
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0;
        high = len(nums) -1 ;
        
        if not nums:
            return "";

        while high >= low:
            mid = (high + low) //2;
            if nums[mid] == target:
                return mid;
            
            if  target > nums[mid]:
                low = mid + 1;
            elif target < nums[mid]:
                high = mid - 1;
        return low;

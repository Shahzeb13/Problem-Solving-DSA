class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return "";
        if len(nums) == 1:
            return nums;
        n = len(nums);
        for i in range(n - 1):
            swapped = False;
            for j in range(n - i -1):
                if nums[j] > nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1], nums[j];
                    swapped = True;
            if not swapped:
                break;
        return nums;

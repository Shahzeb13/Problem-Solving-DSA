class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return "";
        if len(s) == 1:
            return s;
        low = 0;
        high = len(s) - 1;

        while high>low:
            s[low],s[high] = s[high],s[low];
            low += 1;
            high -=1;
        return s;
        

\
class LongestSubString:

    def __init__(self ,s):
        self.s = s;
        self.set = set();
        self.longest = 0;





    def findSubstring(self):

        #Logic
        '''
        Psuedo Code

        set = set();
        longestLength = 0;
        for char in s:
            if char in set:
                set.discard(char);
                # longest -=1;
                set.add(char);
            set.add(char);
            longest += 1;

        
        ===dry run ===
        abcabcbb
        itertion    char      set         longest
            0        a       a             1
            1        b       a,b           2
            2        c       a.b.c         3
            3        A       b,c,a         3
            4        b       c,a,b         3
            5        c       a,b,c         3
            6        b       a,c,b         3
            7        b       a,c,b         3


        Note: The above approacha was just brainstorming!

        I am gona try to sovle this with variable sliding window pattern
        

        ===psuedoCode===
        abcabcbb
        left = 0;
        right = 0
        windowSize = right - left + 1;
        longest = windowSize;
        while right >= left:
            ;
            if s[right] not in set:
                set.add(s[right]);
                right +=1;
                longest = max(longest ,(right - left) + 1);
            else:
                set.discard(s[left]);
                left +=1;
            
        """dry run"""
        abcabcbb
        itr      left       right       val[left]          val[right]       wSize       set
        0          0          0             a                   a             1         {a}
        1          0          1             A                   b             2         {a,b}
        2          0          2             A                   c             3         {abc}
        3          0          3             a                   a             2         {bc}
        4          1          3             b                   a             3         {bca}
        5          1          4             b                   b             2          {ca}
        6          2          4             c                   b             3          {cab} 
        7          2          5             c                   c             2          {ab}
        8          3          5             A                   c             3           {abc}
        9          3          6             a                   b                        {bc}
        10         4          6             b                   b                         {c}
        11         5          6             c                   b                         {cb}
        12         5          7             c                   b                          {b}
        13         6          7             b                   b                          {}
        14         7          7             b                   b                           {b}

        '''
        if not self.s:
            return 0;
        if len(self.s) == 1:
            return 1;
        left = 0;
        right = 0;
        windowSize = (right - left) + 1;
        self.longest = windowSize;
        while right < len(self.s):
            if self.s[right] not in self.set:
                self.set.add(self.s[right]);
                self.longest = max(self.longest, (right - left) + 1);
                right +=1;
            else:
                self.set.discard(self.s[left]);
                left +=1;
        return self.longest;
                


def main():

    s = LongestSubString("abcabcbb");
    output = s.findSubstring();
    print(f"Output: {output}");


if __name__ == "__main__":
    main();

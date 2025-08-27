class MinStack:

    def __init__(self):
        self.stack = [];
        self.minStack = [];

    def push(self, val: int) -> None:
        self.stack.append(val);

    def pop(self) -> None:
        self.stack.pop();

    def top(self) -> int:
        return self.stack[-1];

    def getMin(self) -> int:
        # [1, 2, 0]
        low = 0;
        high = len(self.stack) - 1;
        while high > low:
            # minVal = min(stack[low] , stack[high]);
            if self.stack[low] < self.stack[high]:
                high -= 1;
            else:
                low +=1
        self.minStack.append(min(self.stack[low] , self.stack[high]));
        print(f"MinStack : {self.minStack}");
        print(f"Minimum Value : {self.minStack[-1]}")
        return self.minStack[-1]

    '''
    [-2, -2, -3, -3]
    iteration  low  high   minVal   stack[low]   stack[high]         minStack
       
        0       0    3       -2           -2          -3
        1       1    3       -2           -2          -3
        2       2    3       -3            -3           -3
    '''


def main():
    minStack = MinStack();
    minStack.push(-2);
    minStack.push(-2);
    minStack.push(-3);
    minStack.push(-3);
    print(minStack.stack);
    print(minStack.getMin()); 
    # print(minStack.pop());
    # print(minStack.top());   
    # print(minStack.stack);
    # minStack.getMin();





if __name__ == "__main__":
    main();

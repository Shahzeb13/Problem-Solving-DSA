

class BaseBallGame:


    def __init__(self, operations):
        self.operations = operations;
        self.stack = [];
        self.total = 0;



    def FindScore(self):
        for opr in self.operations:  
            if opr == "C":
                self.stack.pop();  
            elif opr == "D":
                self.stack.append(self.stack[-1] *2);
            elif opr == "+":
                self.stack.append(self.stack[-1] +self.stack[-2]);
            else:
                self.stack.append(int(opr));
        print(self.stack);
        for num in self.stack:
            self.total = self.total + num;
        return self.total;



def main():

    s = BaseBallGame(["5","2","C","D","+"]);
    output = s.FindScore();
    print(output);


if __name__ == "__main__":
    main();
                
        

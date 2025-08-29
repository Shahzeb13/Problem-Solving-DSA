

class ReversePolishNotation:
    def __init__(self , tokens):
        self.tokens = tokens;
        self.stack = [];
        
    

    def Evaluate(self):

        f'''
            ===problem===
            so the problem is that I have been given a string of arithmetic expression in reversed
            polish notation! I have to calculate the result of the expression and then return it

            I am gonna try to solve this by using stack!!!

            ===BrainStorming===
            Let say i push all the element into the stack first
            stack = [ "-" ,"4", "*","3", "+","2","1"] 
            I think this is not right! maybe I will need to reverse the input array first!
            reversed input array = [ "-" ,"4", "*","3", "+","2","1"]
            then stack becomes
            Stack = ["1","2","+","3","*","4","-"],
            NOTE: my stupid ass was appending it in the wrong way ! sorry ! i do not nned to reverse
            not what if I declare an array called operators
            oprs = ["+" , "-" , "*" , "/"]

            now maybe I can use a check while iterating stack that evertime i get an opertaor! i will
            pop all the element including the opertor and calcuilate the suma nd then push that
            into the stack again

            but wait how do I pop all the element before the operator, do i nned some kind of check for that
            ! ony check in my mind is maybe getting the index of the opr and then use that somehow to eval
            the sub expression


            ===psuedoCode===

            Stack = [];
            operatorsRules =  ["+" , "-" , "*" , "/"]
            expressionOperators
            for s in reversed(tokens):
                if s in operatorsRules:
                    expressionOperators.append(s);
                    stack.append(s);
                stack.append(s);

            Stack = ["1","2","+","3","*","4","-"],;
            >>> if i just append operands to the stack then I will not know when to perform operation
            expressionOperators = ["+" , "*" , "-"]
            expressionStr = "";
                for i , val in enumerate(stack):
                if val in operatorsRules:
                    
                    SumResult = calculate sum hhere
                    stack.push(SumResult); here why am i pushing the sumResult back
                    I can literally just loop over stack and then append procedd to concaternate the 
                    element of stack to the already found result
                else:
                    expressionStr += stack.pop();


            ===dry run===

            iteration       s            stackOperation         expression

            0               1                 pop                 "1"
            1               2                 pop                 "1 2"
            2               +                 pop                 "1 2 + = 3"
            3               3                 pop                 "3 3 "
            4               *                 pop                 "3 3 * = 9" 
            5               4                 pop                 "9 4"
            6               -                 pop                  "9 4 - = 5"
            return 5     

            note: before return 5 i should convert it into integer
            and I reme,ber about the divison I need to drop it to zero if its in decimal        
                
                    



        ===psuedo Code===
            operatorsRules =  ["+" , "-" , "*" , "/"]
            for s in tokens:
                if s in operatorsRules:
                    left = stack.pop();
                    right = stack.pop();
                    if s == "+":
                        num = left + right
                    elif s == "-":
                        num = left - right
                    elif s == "*":
                        num = left * right
                    elif s == "/":
                        num = int(left / right)  # truncate toward zero

                    stack.push(num);
                stack.append(s);


        ===dry run===
        ["1","2","+","3","*","4","-"]

        Iteration       s           right         left           num         stack
            0           1                                                   [1]
            1           2                                                   [1,2]
            2           +            2            1              3          [3]
            3           3                                                   [3,3]
            4           *            3            3              6          [9]
            5           4                                                   [9,4]
            6           -            4            9              5         [5]
        



        '''
        
        if not self.tokens:
            return "";

        if len(self.tokens) == 1:
            return int(self.tokens.pop());

        

        operatorsRules =  ["+" , "-" , "*" , "/"]
        for s in self.tokens:
            if s in operatorsRules:
                # print("-----------------------")
                right = self.stack.pop();
                # print(right);
                left = self.stack.pop();
                # print(let)
                if s == "+":
                    num = left + right
                elif s == "-":
                    num = left - right
                elif s == "*":
                    num = left * right
                elif s == "/":
                    num = int(left / right)  # truncate toward zero

                self.stack.append(int(num));
                continue;
            self.stack.append(int(s));
        return self.stack[-1]

      




def main():

    rpn= ReversePolishNotation(["18"]);
    print(f"sum : {rpn.Evaluate()}")

    





if __name__ == "__main__":
    main();

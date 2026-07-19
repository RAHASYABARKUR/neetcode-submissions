class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper_list = ["+","-","*","/"]

        for x in tokens:
            print(stack)
            if x not in oper_list:
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                if(x=="+"):
                    stack.append(a+b)
                elif(x=="-"):
                    stack.append(a-b)
                elif(x=="*"):
                    stack.append(a*b)
                elif(x=="/"):
                    stack.append(int(a/b))
        return stack.pop()
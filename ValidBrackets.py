def function1(a):
        brackets ={ '(' :')' , '{':'}','[':']'}
        stack=[]
        for i in a:
            if i in brackets.keys():
                stack.append(i)
            else:
                if stack and i == brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack
                
        
s = "(]"
# s = "()[]{}"
# s = "["
print(function1(s))
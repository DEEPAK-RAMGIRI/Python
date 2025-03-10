def precedence(i):
    if i == "^": return 3
    elif i == '/' or i == '*': return 2
    elif i == '+' or i=='-': return 1
    else: return -1
def infixtopostfix(exp):
    ans = ""
    stack = []
    for i in exp:
        if i.isalpha():
            ans+=i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                ans+=stack.pop()
            stack.pop()
        else:
            while stack and (precedence(i) <= precedence(stack[-1])):
                ans+=stack.pop()
            stack.append(i)
    while stack:
        ans+=stack.pop()
    return ans
                
            
        
if __name__ == "__main__":
    # exp =  '((A+B)-C*(D/E))+F'
    exp ="a+b*(c^d-e)^(f+g*h)-i"
    print(infixtopostfix(exp))
    
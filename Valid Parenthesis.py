#Problem statement
#You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .



#Return true if the given string 'S' is balanced, else return false.



#For example:
#'S' = "{}()".

#There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
#So the 'S' is Balanced.
#Detailed explanation ( Input/output format, Notes, Images )
#Sample Input 1 :
#[()]{}{[()()]()}
# Sample Output 1 :
# Balanced
# Explanation Of the Sample Input 1 :
# There is always an opening brace before a closing brace i.e. '{' before '}', '(' before '), '[' before ']'.
# So the 'S' is Balanced.
# Sample Input 2 :
# [[}[
# Sample Output 2 :
# Not Balanced
def same(S):
    a=[]
    for i in S:
        if i in "{([":
            a.append(i)
        if i in "})]":
            if i == ')' and a.pop() != '(':
                return False
            elif i== '}' and a.pop() != '{':
                return False
            elif i ==']' and a.pop() != '[':
                return False
    return not a
s="[()]{}{[()()]()}"
# s="[[}{"
print(same(s))

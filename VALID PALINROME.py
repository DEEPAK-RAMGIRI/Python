import re
def function1(s):
    s=re.sub(r'[^a-zA-Z0-9]','',s).lower();
    return s==s[::-1]
sen="A man, a plan, a canal: Panama"
print(function1(sen))
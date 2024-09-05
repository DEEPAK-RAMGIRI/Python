def function1(string1,string2):
    string1=''.join(sorted(string1))
    string2=''.join(sorted(string2))
    return string1 == string2
string1="anagram"
string2="nagaram"
print(function1(string1,string2))
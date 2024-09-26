def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        sets = set()
        result=[]
        s = string[i:i+k]
        for j in s:
            if j not in sets:
                sets.add(j)
                result.append(j)
        print("".join(result))
                
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    # string = 'AABCAAADA" k = 3
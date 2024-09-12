from collections import defaultdict

def groupAnagrams(strs):
    ans = defaultdict(list)
    for i in strs:
        key = ''.join(sorted(i))
        ans[key].append(i)
        
    return ans.values()
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
            
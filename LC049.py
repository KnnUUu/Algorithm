def groupAnagrams(strs):
    dic = dict()
    for str in strs:
        sort_str = ''.join(sorted(str))
        if sort_str in dic:
            dic[sort_str].append(str)
        else:
            dic[sort_str] = [str]
    return [dic[key] for key in dic.keys()]

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
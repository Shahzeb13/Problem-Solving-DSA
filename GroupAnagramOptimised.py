
from collections import defaultdict


def groupAnagram(strs):
    Groups = defaultdict(list);
    for word in strs:
        sortedWord = "".join(sorted(word));
        Groups[sortedWord].append(word);

    return list(Groups.values());







res = groupAnagram(["act", "pots", "tops", "cat", "stop", "hat"])
print(res);

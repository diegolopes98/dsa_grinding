from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        count_char_list = [0] * 26
        for c in s:
            count_char_list[ord(c) - ord("a")] += 1
        res[tuple(count_char_list)].append(s)
    return list(res.values())

from collections import defaultdict
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    fc = defaultdict(int)
    for num in nums:
        fc[num] += 1

    f = [[] for _ in range(len(nums) + 1)]
    for num, count in fc.items():
        f[count].append(num)

    res = []
    for i in range(len(f) - 1, 0, -1):
        if len(res) == k:
            break
        for num in f[i]:
            res.append(num)
            if len(res) == k:
                break
    return res

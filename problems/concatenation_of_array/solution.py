from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * (2 * n)
    for i, num in enumerate(nums):
        ans[i] = num
        ans[i + n] = num
    return ans

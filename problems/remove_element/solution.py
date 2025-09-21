from typing import List


def remove_element(nums: List[int], val: int) -> int:
    l = 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    return l

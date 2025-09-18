def contains_duplicate(nums):
    """
    Given an array of integers nums
    return True or False if contains duplicate or not.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

from collections import deque
from typing import List


def count_students(st: List[int], sw: List[int]) -> int:
    length = len(st)
    stq = deque()
    sws = []

    for i in range(length):
        sws.append(sw[length - i - 1])
        stq.append(st[i])

    last_served = 0
    while len(stq) > 0 and last_served < len(stq):
        if sws[-1] == stq[0]:
            sws.pop()
            stq.popleft()
            last_served = 0
        else:
            stq.append(stq.popleft())
            last_served += 1

    return len(stq)

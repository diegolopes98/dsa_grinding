def is_valid(s: str) -> bool:
    stack = []
    co = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c not in co:
            stack.append(c)
            continue
        if stack and stack[-1] == co[c]:
            stack.pop()
        else:
            return False
    return True if not stack else False

def isAnagra(s, t):
    if len(s) != len(t):
        return False

    s_occurrences = get_char_occurrences(s)
    t_occurrences = get_char_occurrences(t)

    return s_occurrences == t_occurrences


def get_char_occurrences(str):
    occurrences = {}
    for c in str:
        occurrences[c] = occurrences.get(c, 0) + 1
    return occurrences

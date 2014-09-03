"""
Useful tools
"""


def is_sorted(l):
    for i, el in enumerate(l[1:]):
        if el >= l[i-1]:
            return False
    return True
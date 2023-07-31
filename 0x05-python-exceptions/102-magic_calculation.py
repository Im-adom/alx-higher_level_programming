#!/usr/bin/python3
def magic_calculation(a, b):
    ans = 0
    for g in range(1, 3):
        try:
            if g > a:
                raise Exception('Too far')
                ans += a ** b / g
        except Exception:
            ans = b + a
            break
    return ans

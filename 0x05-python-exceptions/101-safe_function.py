#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ans = fct(*args)
        return ans
    except Exception:
        print("Exception:{}".format(sys.exc_ifo()[1]), file=sys.stderr)
        return None

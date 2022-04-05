#!/usr/bin/env python

"""
A basic pandoc filter
"""

from pandocfilters import toJSONFilter, Str
from pdb import set_trace

def foo(key, value, format, meta):
    set_trace()

if __name__ == "__main__":
  toJSONFilter(foo)

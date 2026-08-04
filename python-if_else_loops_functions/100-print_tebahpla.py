#!/usr/bin/python3
"""Prints the alphabet in reverse, alternating lowercase and uppercase."""
for i in range(26):
    print("{}".format(chr(122 - i) if i % 2 == 0 else chr(122 - i).upper()),
          end="")

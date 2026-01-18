#!/usr/bin/env python
import sys

from m17.apps import voipsim

if __name__ == "__main__":
    print(sys.argv)
    voipsim(*sys.argv[1:])

#!/usr/bin/env python
"""This script takes a file path and optionally a URL and generates
 a bigfix prefetch statement."""
# Related:
#  - https://github.com/jgstew/tools/blob/master/Python/url_to_prefetch.py
#  - https://bigfix.me/relevance/details/3022868

#import os
#from hashlib import sha1, sha256


def file_to_prefetch(file_path, url="http://unknown"):
    """Return the bigfix prefetch generated from the provided file"""
    return "TODO: all the things. file:" + file_path + " url:" + url


def main(file_path="LICENSE"):
    """Only called if this script is run directly"""
    print(file_to_prefetch(file_path))

# if called directly, then run this example:
if __name__ == '__main__':
    main()

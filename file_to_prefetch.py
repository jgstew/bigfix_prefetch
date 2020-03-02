#!/usr/bin/env python
"""This script takes a file path and optionally a URL and generates
 a bigfix prefetch statement."""
# Related:
#  - https://github.com/jgstew/tools/blob/master/Python/url_to_prefetch.py
#  - https://bigfix.me/relevance/details/3022868

from __future__ import absolute_import

import os
from hashlib import sha1, sha256


def file_to_prefetch(file_path, url="http://unknown"):
    """Return the bigfix prefetch generated from the provided file"""
    hashes = sha1(), sha256()
    chunksize = max(4*1024, max(h.block_size for h in hashes))

    if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
        print("file exists! " + file_path)
    else:
        return "Error: file does not exist or is not readable! " + file_path

    return "PLACEHOLDER:: file:" + file_path + " url:" + url + \
                " chunksize:" + str(chunksize)
    # return ( "prefetch %s sha1:%s size:%d %s sha256:%s" % \
    #       (filename, hashes[0].hexdigest(), size, url, hashes[1].hexdigest()) )


def main(file_path="LICENSE"):
    """Only called if this script is run directly"""
    print(file_to_prefetch(file_path))

# if called directly, then run this example:
if __name__ == '__main__':
    main()

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
    chunk_size = max(4*1024, max(h.block_size for h in hashes))
    file_size = 0

    if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
        print("Debug_Info:: file exists! " + file_path)
    else:
        return "Error: file does not exist or is not readable! " + file_path
    
    with open(file_path, 'rb') as file_object:
        while True:
            chunk = file_object.read(chunk_size)
            if not chunk:
                break
            # NOTE: This is probably not needed, could read directly from filesystem
            file_size += len(chunk)
            for h in hashes:
                h.update(chunk)


    print("Debug_Info:: file:" + file_path + " url:" + url + \
                " chunksize:" + str(chunk_size))
    return ( "prefetch %s sha1:%s size:%d %s sha256:%s" % \
                (file_path, hashes[0].hexdigest(), file_size, url, hashes[1].hexdigest()) )


def main(file_path="LICENSE"):
    """Only called if this script is run directly"""
    print(file_to_prefetch(file_path))

# if called directly, then run this example:
if __name__ == '__main__':
    main()

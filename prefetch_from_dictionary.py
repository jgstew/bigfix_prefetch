#!/usr/bin/env python
"""This script takes a python dictionary and formats it into a bigfix prefetch

This is the opposite of parse_prefech.py
"""

from __future__ import absolute_import

FORMAT_PREFETCH_STATEMENT = "prefetch {file_name} sha1:{file_sha1} \
size:{file_size} {download_url}"
FORMAT_PREFETCH_BLOCK_ITEM = "add prefetch item name={file_name} sha1={file_sha1} size={file_size} \
url={download_url}"

def prefetch_from_dictionary(prefetch_dictionary, prefetch_type=None):
    """Turn Python Dictionary into BigFix Prefetch String"""
    if not prefetch_type:
        if 'prefetch_type' in prefetch_dictionary:
            prefetch_type = prefetch_dictionary['prefetch_type']
        else:
            # default to 'statement' if no other type given
            prefetch_type = 'statement'

    # prefetch_type must be either `block` or `statement`
    print(prefetch_type)

    if prefetch_type == 'block':
        print(FORMAT_PREFETCH_BLOCK_ITEM)
    else:
        print(FORMAT_PREFETCH_STATEMENT)

    # if sha256, then append it to string
    return prefetch_dictionary

def main():
    """Only called if this script is run directly"""
    prefetch_dictionary = {
                'file_name': 'unzip.exe',
                'file_size': '167936',
                'file_sha1': 'e1652b058195db3f5f754b7ab430652ae04a50b8',
                'download_url': 'http://software.bigfix.com/download/redist/unzip-5.52.exe'
                }
    print(prefetch_from_dictionary(prefetch_dictionary))
    prefetch_dictionary['prefetch_type'] = "block"
    print(prefetch_from_dictionary(prefetch_dictionary))

# if called directly, then run this example:
if __name__ == '__main__':
    main()

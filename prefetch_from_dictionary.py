#!/usr/bin/env python
"""This script takes a python dictionary and formats it into a bigfix prefetch

This is the opposite of parse_prefech.py
"""

from __future__ import absolute_import

def prefetch_from_dictionary(prefetch_dictionary, prefetch_type=None):
    if not prefetch_type:
        if 'prefetch_type' in prefetch_dictionary:
            prefetch_type = prefetch_dictionary['prefetch_type']
        else:
            prefetch_type = 'statement'

    # prefetch_type must be either `block` or `statement`
    print(prefetch_type)

    return prefetch_dictionary

def main():
    """Only called if this script is run directly"""
    prefetch_dictionary = {
                'file_name': 'LGPO.zip',
                'file_size': '815660',
                'file_sha1': '0c74dac83aed569607aaa6df152206c709eef769',
                'download_url': \
'https://download.microsoft.com/download/8/5/C/85C25433-A1B0-4FFA-9429-7E023E7DA8D8/LGPO.zip',
                'file_sha256': '6ffb6416366652993c992280e29faea3507b5b5aa661c33ba1af31f48acea9c4'
                }
    print(prefetch_from_dictionary(prefetch_dictionary))

# if called directly, then run this example:
if __name__ == '__main__':
    main()
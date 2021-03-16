#!/usr/bin/env python
"""
This script takes a bigfix prefetch and validates it

BigFix Prefetches:
    - Must have size
        - int or int(string) greater than 0
    - Must have sha1 if prefetch statement, always expected (except-invalid-prefetch-statement)
        - prefetch blocks do NOT require SHA1 (warn-optional-missing)
        - string of exactly 40 characters - case insensitive
    - Must have sha256 to work with enhanced security (warn-optional-missing)
        - string of exactly 64 characters - case insensitive

If enhanced security is a requirement, then SHA256 warnings become exceptions

MD5 is never used, only provided for use with IOCs or similar weak validation
"""

import warnings

import parse_prefetch


def validate_prefetch(bigfix_prefetch, sha256_required=False):
    """Validate the BigFix Prefetch"""
    # if prefetch_one is not a dictionary, then parse it into one
    if 'file_size' in bigfix_prefetch:
        parsed_bigfix_prefetch = bigfix_prefetch
    else:
        parsed_bigfix_prefetch = parse_prefetch.parse_prefetch(bigfix_prefetch)
    
    if not int(parsed_bigfix_prefetch['file_size']) > 0:
        warnings.warn("size is invalid")
        return False
    
    return True


def main():
    """Only called if this script is run directly"""
    prefetch_dictionary_valid = {
        'file_name': 'unzip.exe',
        'file_size': '167936',
        'file_sha1': 'e1652b058195db3f5f754b7ab430652ae04a50b8',
        'file_sha256': '8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a',
        'download_url': 'http://software.bigfix.com/download/redist/unzip-5.52.exe'
    }
    print(validate_prefetch(prefetch_dictionary_valid))
    print(validate_prefetch("add prefetch item name=unzip.exe sha256=8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a size=167936 url=http://software.bigfix.com/download/redist/unzip-5.52.exe"))
    print(validate_prefetch("add prefetch item name=unzip.exe sha256=8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a size=0 url=http://software.bigfix.com/download/redist/unzip-5.52.exe"))


# if called directly, then run this example:
if __name__ == '__main__':
    main()

#!/usr/bin/env python
"""
This script takes 2 prefetch statements, blocks, or dictionaries and validates they match
"""

import parse_prefetch


def prefetches_have_matching_hashes(prefetch_one, prefetch_two):  # pylint: disable=too-many-branches
    """Compare the file size and hashes to make sure they match"""
    if 'file_size' in prefetch_one:
        parsed_prefetch_one = prefetch_one
    else:
        parsed_prefetch_one = parse_prefetch.parse_prefetch(prefetch_one)

    if 'file_size' in prefetch_two:
        parsed_prefetch_two = prefetch_two
    else:
        parsed_prefetch_two = parse_prefetch.parse_prefetch(prefetch_two)

    # ensure both prefetches have the required details
    if not (
            ("file_size" in parsed_prefetch_one and "file_sha1" in parsed_prefetch_one) and
            ("file_size" in parsed_prefetch_two and "file_sha1" in parsed_prefetch_two)
    ):
        print("invalid prefetch")
        if (
                ("file_size" in parsed_prefetch_one and "file_md5" in parsed_prefetch_one) and
                ("file_size" in parsed_prefetch_two and "file_md5" in parsed_prefetch_two)
        ):
            print("Both Have MD5 - Is this for comparison?")
        return False

    try:
        # file_size could be an int or a string, force convertion to int for comparison.
        if int(parsed_prefetch_one['file_size']) == int(parsed_prefetch_two['file_size']):
            if parsed_prefetch_one['file_sha1'] == parsed_prefetch_two['file_sha1']:
                if (
                        ("file_sha256" in parsed_prefetch_one)
                        and
                        ("file_sha256" in parsed_prefetch_two)
                ):
                    # NOTE: need to also check sha256 if present
                    if parsed_prefetch_one['file_sha256'] == parsed_prefetch_two['file_sha256']:  # pylint: disable=no-else-return
                        return True
                    else:
                        print("ERROR: file_sha256 doesn't match")
                        return False
                else:
                    print("Warning: file_sha256 is missing but size and sha1 match")
                    return True
            else:
                print("ERROR: file_sha1 doesn't match")
        else:
            print("ERROR: file_size doesn't match")
    except ValueError:
        print("ERROR: Invalid file_size")
        return False

    # catch all:
    return False


def main():
    """Only called if this script is run directly"""
    prefetch_dictionary_one = {
        'file_name': 'unzip.exe',
        'file_size': '167936',
        'file_sha1': 'e1652b058195db3f5f754b7ab430652ae04a50b8',
        'file_sha256': '8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a',
        'download_url': 'http://software.bigfix.com/download/redist/unzip-5.52.exe'
    }
    print(
        prefetches_have_matching_hashes(prefetch_dictionary_one, prefetch_dictionary_one)
    )


# if called directly, then run this example:
if __name__ == '__main__':
    main()

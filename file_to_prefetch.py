
# Related:
#  - https://github.com/jgstew/tools/blob/master/Python/url_to_prefetch.py
#  - https://bigfix.me/relevance/details/3022868

import os
from hashlib import sha1, sha256


def file_to_prefetch(file_path):
    return "TODO: all the things " + file_path


def main(file_path="LICENSE"):
    print(file_to_prefetch(file_path))

# if called directly, then run this example:
if __name__ == '__main__':
    main()

"""test bigfix_prefetch"""

import os.path
import site
import sys

# https://stackoverflow.com/questions/34846584/whats-the-recommended-way-to-import-unittest-or-unittest2-depending-on-pyth/66616071
# try:
#    import unittest2 as unittest
# except ImportError:
#    import unittest

# add module folder to import paths
site.addsitedir(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
)

import bigfix_prefetch  # pylint: disable=import-error,wrong-import-position

# pylint: disable=line-too-long

EXAMPLES_BAD = [
    # 0 size is wrong
    "add prefetch item name=unzip.exe sha256=8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a size=0 url=http://software.bigfix.com/download/redist/unzip-5.52.exe",
    # size must be an integer
    "add prefetch item name=unzip.exe sha256=8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a size=ABC url=http://software.bigfix.com/download/redist/unzip-5.52.exe",
    # size must be a positive integer
    "add prefetch item name=unzip.exe sha256=8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a size=-1 url=http://software.bigfix.com/download/redist/unzip-5.52.exe",
    # sha1 must be 40 characters
    "add prefetch item name=unzip.exe sha1=8d9b5190aace52a size=55 url=http://software.bigfix.com/download/redist/unzip-5.52.exe",
    # sha256 must be 64 characters
    "add prefetch item name=unzip.exe sha256=8d9b5190aace52a1db1ac73a65ee9999c329157 size=55 url=http://software.bigfix.com/download/redist/unzip-5.52.exe",
    "add prefetch item name=unzip.exe sha1=4cbd040533a2f43f sha256=8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a size=55 url=http://software.bigfix.com/download/redist/unzip-5.52.exe",
]

EXAMPLES_GOOD = [
    {
        'file_name': 'unzip.exe',
        'file_size': '167936',
        'file_sha1': 'e1652b058195db3f5f754b7ab430652ae04a50b8',
        'file_sha256': '8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a',

        'download_url': 'http://software.bigfix.com/download/redist/unzip-5.52.exe'
    },
    "add prefetch item name=unzip.exe sha256=8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a size=167936 url=http://software.bigfix.com/download/redist/unzip-5.52.exe",
    "prefetch file.txt sha1:4cbd040533a2f43fc6691d773d510cda70f4126a size:5 http://unknown sha256:41af286dc0b172ed2f1ca934fd2278de4a1192302ffa07087cea2682e7d372e3",
]

# pylint: enable=line-too-long

tests_count = 0  # pylint: disable=invalid-name


for i in EXAMPLES_GOOD:
    tests_count += 1
    print(i)
    assert bigfix_prefetch.prefetch_validate(i) is True

for i in EXAMPLES_BAD:
    tests_count += 1
    print(i)
    assert bigfix_prefetch.prefetch_validate(i) is False


# tests pass, return 0:
print("Success: %d Tests pass" % tests_count)
sys.exit(0)

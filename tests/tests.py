"""test bigfix_prefetch"""
# pylint: disable=import-error,wildcard-import,undefined-variable,wrong-import-position,R0801
import argparse
import os.path
import site
import sys


# don't create bytecode for tests because it is cluttery in python2
sys.dont_write_bytecode = True

# https://stackoverflow.com/questions/34846584/whats-the-recommended-way-to-import-unittest-or-unittest2-depending-on-pyth/66616071
# try:
#    import unittest2 as unittest
# except ImportError:
#    import unittest

# check for --test_pip arg
parser = argparse.ArgumentParser()
parser.add_argument("--test_pip", help="to test package installed with pip",
                    action="store_true")
args = parser.parse_args()

if not args.test_pip:
    # add module folder to import paths for testing local src
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
    )
    sys.path.reverse()

from bigfix_prefetch import *

from bigfix_prefetch.prefetch_validate import validate_prefetch  # pylint: disable=import-error

print(prefetch_validate.__file__)

# make sure we are testing the right place:
if args.test_pip:
    # this will fail on windows
    assert "/src/bigfix_prefetch/prefetch_validate.py" not in prefetch_validate.__file__

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
    # sha1 must be 40 characters
    "add prefetch item name=unzip.exe sha1=4cbd040533a2f43f sha256=8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a size=55 url=http://software.bigfix.com/download/redist/unzip-5.52.exe",
    # sha256 must be 64 characters
    {
        'file_name': 'unzip.exe',
        'file_size': '167936',
        'file_sha1': 'e1652b058195db3f5f754b7ab430652ae04a50b8',
        'file_sha256': '8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4aQQ',

        'download_url': 'http://software.bigfix.com/download/redist/unzip-5.52.exe'
    },
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
    "add prefetch item name=unzip.exe sha1=e1652b058195db3f5f754b7ab430652ae04a50b8 size=167936 url=http://software.bigfix.com/download/redist/unzip-5.52.exe",
    "prefetch file.txt sha1:4cbd040533a2f43fc6691d773d510cda70f4126a size:5 http://unknown sha256:41af286dc0b172ed2f1ca934fd2278de4a1192302ffa07087cea2682e7d372e3",
    # for some reason this is bad on ubuntu when the module is installed with pip? need to investigate.
    "prefetch google.com sha1:f5c694d8dc2804e1fa61515a40b4088e5cd0b91c size:13794 http://google.com/google.com sha256:6378c533fa5224f21b177e72f172a949a5b16c6aad9be625435a0a797c0d31b0",
]

tests_count = 0  # pylint: disable=invalid-name


for i in EXAMPLES_GOOD:
    #print(i)
    tests_count += 1
    assert prefetch_validate.validate_prefetch(i) is True
    tests_count += 1
    assert prefetches_have_matching_hashes.prefetches_have_matching_hashes(i, i) is True
    tests_count += 1
    assert validate_prefetch(i) is True

for i in EXAMPLES_BAD:
    tests_count += 1
    #print(i)
    assert prefetch_validate.validate_prefetch(i) is False

# test 2 equivalent:
tests_count += 1
assert prefetches_have_matching_hashes.prefetches_have_matching_hashes(EXAMPLES_GOOD[0], EXAMPLES_GOOD[1]) is True
tests_count += 1
assert prefetches_have_matching_hashes.prefetches_have_matching_hashes(EXAMPLES_GOOD[0], EXAMPLES_GOOD[2]) is True

# test bad comparison due to no matching hashes:
tests_count += 1
assert prefetches_have_matching_hashes.prefetches_have_matching_hashes(EXAMPLES_GOOD[1], EXAMPLES_GOOD[2]) is False


# pylint: disable=line-too-long

# test against known output
tests_count += 1
assert prefetch_from_dictionary.prefetch_from_dictionary(EXAMPLES_GOOD[0]) == "prefetch unzip.exe sha1:e1652b058195db3f5f754b7ab430652ae04a50b8 size:167936 http://software.bigfix.com/download/redist/unzip-5.52.exe sha256:8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a"

# test against known output
tests_count += 1
assert prefetch_from_dictionary.prefetch_from_dictionary(EXAMPLES_GOOD[0], "block") == "add prefetch item name=unzip.exe sha1=e1652b058195db3f5f754b7ab430652ae04a50b8 size=167936 url=http://software.bigfix.com/download/redist/unzip-5.52.exe sha256=8d9b5190aace52a1db1ac73a65ee9999c329157c8e88f61a772433323d6b7a4a"

# test against known output
tests_count += 1
assert "prefetch tests.py " in prefetch_from_file.file_to_prefetch(os.path.abspath(__file__))

# test against known output
# NOTE: This is will actually get the file from the internet, which could be slow or fail for transient network reasons
# tests_count += 1
# assert bigfix_prefetch.prefetch.prefetch(EXAMPLES_GOOD[0], False) is True

# tests pass, return 0:
print("-------------------------------------")

print("Success: %d Tests pass" % tests_count)
print("")
sys.exit(0)

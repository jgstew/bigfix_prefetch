#!/usr/bin/env python
"""
function url_to_prefetch(url) takes
    Input a URL of a file
        downloads the file at the URL, and
    Outputs a BigFix Prefetch statement.
"""

# NOTE: Consider adding options to cache the file downloads & log/cache the prefetches generated

import posixpath
from hashlib import sha1, sha256

try:
    from urllib.request import urlopen # Python 3
except ImportError:
    from urllib2 import urlopen # Python 2

from prefetch_from_dictionary import prefetch_from_dictionary

def main():
    """Only called if this script is run directly"""
    if len(sys.argv) == 2:
        print(url_to_prefetch(sys.argv[1]))
    else:
        print(url_to_prefetch(
            "https://download.microsoft.com/download/8/5/C/85C25433-A1B0-4FFA-9429-7E023E7DA8D8/LGPO.zip"
            ))

def url_to_prefetch(url):
    """stream down file from url and calculate size & hashes, output BigFix prefetch"""
    prefetch_dictionary = {}
    hashes = sha1(), sha256()
    # chunksize seems like it could be anything
    #   it is probably best if it is a multiple of a typical hash block_size
    #   a larger chunksize is probably best for faster downloads
    chunksize = max(384000, max(a_hash.block_size for a_hash in hashes))
    size = 0

    # NOTE: handle other cases, ensure default name if none set
    filename = posixpath.basename(url)

    response = urlopen(url)
    # NOTE: Get Header If Present for Download Estimate:
    #               int(req.info().getheader('Content-Length').strip())
    while True:
        chunk = response.read(chunksize)
        if not chunk:
            break
        size += len(chunk)
        for a_hash in hashes:
            a_hash.update(chunk)

    prefetch_dictionary['file_name'] = filename
    prefetch_dictionary['file_size'] = size
    prefetch_dictionary['file_sha1'] = hashes[0].hexdigest()
    prefetch_dictionary['file_sha256'] = hashes[1].hexdigest()
    prefetch_dictionary['download_url'] = url

    return prefetch_from_dictionary(prefetch_dictionary)

    # https://www.learnpython.org/en/String_Formatting
    #return "prefetch %s sha1:%s size:%d %s sha256:%s" % \
    #            (filename, hashes[0].hexdigest(), size, url, hashes[1].hexdigest())


# if called directly, then run this example:
if __name__ == '__main__':
    import sys
    main()

# References:
# https://stackoverflow.com/questions/1517616/stream-large-binary-files-with-urllib2-to-file
# https://gist.github.com/Zireael-N/ed36997fd1a967d78cb2

#  AWS Lambda
#from url_to_prefetch import url_to_prefetch
#def lambda_handler(event, context):
#    print( event['url_to_prefetch'] )
#    return url_to_prefetch( event['url_to_prefetch'] )

#  function url_to_prefetch(url) takes
#    Input a URL of a file
#      downloads the file at the URL, and 
#    Outputs a BigFix Prefetch statement.

##  Example Results:
# Docker: docker run python:2 bash -c "wget https://raw.githubusercontent.com/jgstew/tools/master/url_to_prefetch.py ;python url_to_prefetch.py"
#  Input: http://download.windowsupdate.com/d/msdownload/update/software/secu/2016/07/windows10.0-kb3172729-x64_18df742fad6bebc01e617c2d4f92e0d325e5138f.msu
# Output: prefetch testfile sha1:18df742fad6bebc01e617c2d4f92e0d325e5138f size:199259 http://download.windowsupdate.com/d/msdownload/update/software/secu/2016/07/windows10.0-kb3172729-x64_18df742fad6bebc01e617c2d4f92e0d325e5138f.msu sha256:f5b55d436056a905e755984d457bac67295ad3e11531a6c33f3812cfb63ce010

# TODO: Consider adding options to cache the file downloads & log/cache the prefetches generated

import posixpath
from hashlib import sha1, sha256

try:
  from urllib.request import urlopen # Python 3
except ImportError:
  from urllib2 import urlopen # Python 2


def main():
  print( url_to_prefetch("http://download.windowsupdate.com/d/msdownload/update/software/secu/2016/07/windows10.0-kb3172729-x64_18df742fad6bebc01e617c2d4f92e0d325e5138f.msu") )

def url_to_prefetch(url):
  hashes = sha1(), sha256()
  # chunksize seems like it could be anything
  #   it is probably best if it is a multiple of a typical hash block_size
  #   a larger chunksize is probably best for faster downloads
  chunksize = max(384000, max(h.block_size for h in hashes))
  size = 0

  # TODO: handle other cases, ensure default name if none set
  filename = posixpath.basename(url)
  
  response = urlopen(url)
  # TODO: Get Header If Present for Download Estimate:  int(req.info().getheader('Content-Length').strip())
  while True:
    chunk = response.read(chunksize)
    if not chunk:
      break
    size += len(chunk)
    for h in hashes:
      h.update(chunk)

  # https://www.learnpython.org/en/String_Formatting
  return ( "prefetch %s sha1:%s size:%d %s sha256:%s" % (filename, hashes[0].hexdigest(), size, url, hashes[1].hexdigest()) )


# if called directly, then run this example:
if __name__ == '__main__':
  main()


# References: 
#  - https://stackoverflow.com/questions/537542/how-can-i-create-multiple-hashes-of-a-file-using-only-one-pass
#  - https://stackoverflow.com/questions/1517616/stream-large-binary-files-with-urllib2-to-file
#  - https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
#  - https://gist.github.com/Zireael-N/ed36997fd1a967d78cb2
#  - https://blog.sourcerer.io/full-guide-to-developing-rest-apis-with-aws-api-gateway-and-aws-lambda-d254729d6992
#  - https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-lambda.html

#  AWS Lambda
#from url_to_prefetch import url_to_prefetch
#def lambda_handler(event, context):
#    print( event['url_to_prefetch'] )
#    return url_to_prefetch( event['url_to_prefetch'] )


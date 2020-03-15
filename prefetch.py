#!/usr/bin/env python
"""This script takes a bigfix prefetch and downloads the file

The downloaded file will be validated against the prefetch statement

This validates both the prefetch and the resulting file downloaded are still valid

Validation Steps: Size, SHA1, SHA256  (warn if sha256 is not present, but generate it)

This script accepts a prefetch statement, or prefetch block, or a dictionary with prefetch info
"""
# Related:
#  - https://github.com/jgstew/tools/blob/master/Python/url_to_prefetch.py

import parse_prefech

def prefetch(prefetch_data, save_file=True):
    """actually prefetch the file and validate the file and prefetch data"""
    parsed_prefetch = {}
    file_path = ""

    if 'file_size' in prefetch_data:
        parsed_prefetch = prefetch_data
    else:
        parsed_prefetch = parse_prefech.parse_prefetch(prefetch_data)
    # NOTE: do the download & validation (url_to_prefetch)
    
    # if file_path doesn't exist, then use file_name and current directory
    #  if file doesn't exist, then download file there
    #  then validate it against prefetch data
    
    if 'file_path' in parsed_prefetch:
        file_path = parsed_prefetch['file_path']
    else:
        file_path = parsed_prefetch['file_name']

    if save_file:
        print(file_path)

    return parsed_prefetch

def main():
    """Only called if this script is run directly"""
    print(prefetch("add prefetch item name=LGPO.zip sha1=0c74dac83aed569607aaa6df152206c709eef769 \
size=815660 url=https://download.microsoft.com/download/8/5/C/85C25433-A1B0-4FFA-9429-7E023E7DA8D8/LGPO.zip \
sha256=6ffb6416366652993c992280e29faea3507b5b5aa661c33ba1af31f48acea9c4"))
    print(prefetch("prefetch unzip.exe sha1:e1652b058195db3f5f754b7ab430652ae04a50b8 \
size:167936 http://software.bigfix.com/download/redist/unzip-5.52.exe"))
    parsed_prefetch = {
                'file_name': 'LGPO.zip',
                'file_size': '815660',
                'file_sha1': '0c74dac83aed569607aaa6df152206c709eef769',
                'download_url': \
'https://download.microsoft.com/download/8/5/C/85C25433-A1B0-4FFA-9429-7E023E7DA8D8/LGPO.zip',
                'file_sha256': '6ffb6416366652993c992280e29faea3507b5b5aa661c33ba1af31f48acea9c4'
                }
    print(prefetch(parsed_prefetch))


# if called directly, then run this example:
if __name__ == '__main__':
    main()

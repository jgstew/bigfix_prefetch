# bigfix-prefetch
Python scripts for working with BigFix prefetches

[Tested](https://github.com/jgstew/bigfix_prefetch/actions/workflows/test_src.yaml) on Mac, Windows, Linux on Python 3

This does theoretically support Python2 but is no longer tested and validated for Python2.

## Install through pip

`pip install bigfix-prefetch`

- https://pypi.org/project/bigfix-prefetch/


## Prefetch Regex

For either prefetches or prefetch block items:

This assumes prefetch block items can appear in any order, and you already have a line that only contains the prefetch text.

Name of file: ` *(prefetch |add prefetch item .*name=)(\S+) `
Size: ` *(prefetch |add prefetch item ).*size(=|:)(\d+)( |\b)`
SHA1: ` *(prefetch |add prefetch item ).*sha1(=|:)(\S{40})( |\b)`
SHA256: ` *(prefetch |add prefetch item ).*sha256(=|:)(\S{64})( |\b)`
URL: ` *(prefetch .* (http\S+)|add prefetch item .*url=(\S+))( |\b)`
- Prefetch block: ` *add prefetch item .*url=(\S+)( |\b)`
- Prefetch: ` *prefetch .*size:\d+ (\S+)( |\b)`

See also: src/bigfix_prefetch/prefetch_parse.py

## Related:
- https://github.com/jgstew/generate_bes_from_template

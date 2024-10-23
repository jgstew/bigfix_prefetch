"""
import functions so they can be run as the module
"""

from . import (
    prefetch,
    prefetch_from_dictionary,
    prefetch_from_file,
    prefetch_from_url,
    prefetch_parse,
    prefetch_validate,
    prefetches_have_matching_hashes,
)

__version__ = "1.1.4"

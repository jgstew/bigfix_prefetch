"""
To run this module directly
"""

# pylint: disable=no-else-return
import argparse
import os

try:
    from . import prefetch_from_file
except ImportError:
    import prefetch_from_file

try:
    from . import prefetch_from_url
except ImportError:
    import prefetch_from_url


def validate_filepath_or_url(filepath_or_url=""):
    """validate string is filepath or URL"""
    if ("://" in filepath_or_url) or (
        os.path.isfile(filepath_or_url) and os.access(filepath_or_url, os.R_OK)
    ):
        return filepath_or_url
    else:
        raise ValueError(filepath_or_url)


def build_argument_parser():
    """Build and return the argument parser."""

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "filepath_or_url",
        nargs="?",
        type=validate_filepath_or_url,
        default="bigfix_prefetch/__init__.py",
        help="Path to file or URL to create prefetch for.",
    )
    parser.add_argument(
        "--prefetch-block",
        default=False,
        action="store_true",
        help="generate a prefetch block instead of prefetch statement",
    )
    parser.add_argument(
        "--override-url",
        default="http://localhost/unknown",
        help="URL to use in prefetch statement if providing file path",
    )

    return parser


def main(argv=None):
    """execution starts here"""
    # print("bigfix_prefetch __main__ main()")

    # Parse command line arguments.
    argparser = build_argument_parser()
    args = argparser.parse_args(argv)

    try:
        prefetch_result = prefetch_from_file.file_to_prefetch(
            args.filepath_or_url, args.override_url
        )
        print(prefetch_result)
        return prefetch_result
    except FileNotFoundError:
        prefetch_result = prefetch_from_url.url_to_prefetch(args.filepath_or_url)
        print(prefetch_result)
        return prefetch_result


main()

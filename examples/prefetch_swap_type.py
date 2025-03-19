"""
This will swap the type of bigfix prefetch, from block to statement or statement to block.
"""

import argparse
import sys

import bigfix_prefetch


def main(prefetch_to_swap):
    """Only called if this script is run directly"""
    if not bigfix_prefetch.prefetch_validate.validate_prefetch(prefetch_to_swap):
        print("ERROR: Invalid prefetch")
        return 1

    parsed = bigfix_prefetch.prefetch_parse.parse_prefetch(prefetch_to_swap)

    # get the type of the prefetch input
    prefetch_type = parsed["prefetch_type"]

    # swap the type of the prefetch
    if prefetch_type == "block":
        prefetch_type = "statement"
    else:
        prefetch_type = "block"

    # get the rest of the prefetch swap
    swapped = bigfix_prefetch.prefetch_from_dictionary.prefetch_from_dictionary(
        parsed, prefetch_type
    )

    print(swapped)

    return 0


# if called directly, then run this example:
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Swap the type of BigFix prefetch.")
    parser.add_argument("prefetch", help="The prefetch string to swap.")
    args = parser.parse_args()

    # add prefetch item name=7z2409-x64.exe sha1=28b53835fe92c3fa6e0c422fc3b17c6bc1cb27e0 size=1637343 url=https://www.7-zip.org/a/7z2409-x64.exe sha256=bdd1a33de78618d16ee4ce148b849932c05d0015491c34887846d431d29f308e
    sys.exit(main(args.prefetch))

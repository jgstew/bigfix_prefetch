"""
This example is how to update a prefetch to add sha256 hashes to a prefetch.

This WILL cause the file to be downloaded over the internet in the prefetch, though the file will not be saved to disk by default.
"""

# NOTE: this example requires bigfix_prefetch 1.1.4+
import bigfix_prefetch


def main():
    """Only called if prefetch is run directly"""
    prefetch_to_update = "prefetch unzip.exe sha1:e1652b058195db3f5f754b7ab430652ae04a50b8 size:167936 http://software.bigfix.com/download/redist/unzip-5.52.exe"

    # get prefetch type: (block or statement)
    parsed = bigfix_prefetch.prefetch_parse.parse_prefetch(prefetch_to_update)

    # get updated prefetch: (the False means the file will not be saved to disk)
    updated_prefetch = bigfix_prefetch.prefetch.prefetch(prefetch_to_update, False)

    updated_prefetch["prefetch_type"] = parsed["prefetch_type"]

    print("Updated Prefetch:")
    print(
        bigfix_prefetch.prefetch_from_dictionary.prefetch_from_dictionary(
            updated_prefetch
        )
    )


# if called directly, then run this example:
if __name__ == "__main__":
    main()

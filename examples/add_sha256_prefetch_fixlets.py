"""
This example is how to update a prefetch to add sha256 hashes to a prefetch.

This WILL cause the file to be downloaded over the internet in the prefetch, though the file will not be saved to disk by default.
"""

import re

# pylint: disable=import-error
import besapi

# NOTE: this example requires bigfix_prefetch 1.1.5+
import bigfix_prefetch


def update_fixlet_prefetch(file_path):
    """update fixlet files"""
    print("update_fixlet_prefetch(file_path)")

    file_contents = ""

    # read file contents
    with open(file_path, "r", encoding="utf-8") as file:
        # Reading from a file
        file_contents = file.read()
        # print(file_contents)

        # extract prefetch statement (or block?)
        prefetches = re.findall(".*prefetch.*$", file_contents, re.MULTILINE)
        for prefetch in prefetches:
            prefetch = prefetch.strip()
            # print(bigfix_prefetch.prefetch_parse.parse_prefetch(prefetch))

            # update prefetch
            # pylint: disable=broad-exception-caught
            # catching broad exception on purpose in case of parsing error
            try:
                updated_prefetch = bigfix_prefetch.prefetch.add_sha256_prefetch(
                    prefetch
                )
            except BaseException as err:
                print(f"ERROR with prefetch: {prefetch}")
                print(err)
                continue

            file_contents = file_contents.replace(prefetch, updated_prefetch)

            # print(file_contents)

    # write updated file contents back
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(file_contents)

    # validate changed bes file with validate-bex-xml module before upload
    # consider writing updated fixlets back to root server
    return file_path


def main():
    """Only called if this script is run directly"""

    bes_conn = besapi.besapi.get_bes_conn_using_config_file()

    fixlets_to_fix_relevance = """ ("fixlet/custom/" & name of site of it & "/" & id of it as string) of fixlets whose( (fixlet flag of it OR task flag of it) AND exists scripts whose(it as lowercase contains "prefetch" AND it as lowercase does not contain "sha256") of actions of it ) of bes custom sites whose(name of it = "Demo") """

    results = bes_conn.session_relevance_array(fixlets_to_fix_relevance)

    print(results)

    for fixlet in results:
        # https://developer.bigfix.com/rest-api/api/fixlet.html
        export_file_path = bes_conn.export_item_by_resource(
            fixlet, "./examples/fixlets_to_fix"
        )
        print(export_file_path)
        update_fixlet_prefetch(export_file_path)


# if called directly, then run this example:
if __name__ == "__main__":
    main()

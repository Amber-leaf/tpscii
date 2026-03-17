import binascii
import json
import sys


def lookup_encoding(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def main():
    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1], "r") as f:
            byte_input = f.read()
    else:
        # Read from stdin
        print(
            "Paste text to decode, then press Ctrl+D (Unix) or Ctrl+Z (Windows) when done:"
        )
        byte_input = sys.stdin.read()

    byte_input = byte_input.lower().strip().replace("0x", "")  # cleanup bytes

    out = ""

    pages = []
    current_page = 0

    sequence_accumulator = ""
    i = 0

    byte_input = [
        byte_input[i : i + 2] for i in range(0, len(byte_input), 2)
    ]  # Split into bytes.

    encoding_json = json.loads(open("encoding.json").read())

    for page in encoding_json:
        pages.append(page)

    while i < len(byte_input):
        byte = int(byte_input[i].strip().lower(), 16)

        match byte:
            case 0xFF:  # page sequence
                # print("page sequence")
                current_page = int(
                    byte_input[i + 1].strip().lower()
                    + byte_input[i + 2].strip().lower(),
                    16,
                )
                i += 3
                continue
            case 0xFE:  # proper noun sequence
                sequence_accumulator = ""
                i += 1
                try:
                    next_byte = byte_input[i].strip().lower()
                    # print(f"next byte: {next_byte}")
                    # print(f"sequence accumulator: {sequence_accumulator}")
                except IndexError:
                    exit(f"Bad PNT sequence at {i}!")
                while next_byte != "fe":
                    if int(next_byte, 16) > 0x3F:
                        sequence_accumulator += lookup_encoding(
                            encoding_json["page" + str(current_page)], "0x" + next_byte
                        )[0]
                    i += 1
                    try:
                        next_byte = byte_input[i].strip().lower()
                        # print(f"next byte: {next_byte}")
                        # print(f"sequence accumulator: {sequence_accumulator}")
                    except IndexError:
                        exit(f"Bad PNT sequence at {i}!")

                out += sequence_accumulator.title()
                # print("done")
                i += 1
                continue
            case _:  # default
                if byte <= 0x3F and current_page == 0:
                    # print(f"ascii: {binascii.unhexlify(byte_input[i].strip().lower()).decode(
                    #   "utf-8"
                    # )}")
                    out += binascii.unhexlify(byte_input[i].strip().lower()).decode(
                        "utf-8"
                    )
                    i += 1
                    continue
                else:
                    # print(f"normal: {lookup_encoding(
                    #    encoding_json["page" + str(current_page)],
                    #    "0x" + byte_input[i].strip().lower(),
                    # )}")
                    out += lookup_encoding(
                        encoding_json["page" + str(current_page)],
                        "0x" + byte_input[i].strip().lower(),
                    )
                    i += 1
                    continue

    print(f"TPSCII decoding for '0x{"".join(byte_input)}':\n{out}")


if __name__ == "__main__":
    main()

import binascii
import json
import sys

def get_key_from_value(dictionary, value):
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

    byte_input = byte_input.lower().strip().replace("0x", "") # cleanup bytes

    out = ""

    pages = []
    current_page = 0

    in_switch_sequence = False
    page_switch_target = ""

    byte_input = [byte_input[i : i + 2] for i in range(0, len(byte_input), 2)]  # Split into bytes.

    encoding_json = json.loads(open("encoding.json").read())

    for page in encoding_json:
        pages.append(page)

    for i in range(len(byte_input)):
        byte = byte_input[i].strip().lower()

        if in_switch_sequence:
            if len(page_switch_target) >= 4: # done with page switch
                in_switch_sequence = False
                current_page = int("".join(page_switch_target))
                page_switch_target = ""
            else:
                page_switch_target += byte

        if byte == "ff": # start page switch
            in_switch_sequence = True
        elif (int(byte, 16) <= 0x20 or int(byte, 16) == 0x50) and not in_switch_sequence:  # ASCII codepoint
            out += binascii.unhexlify(byte).decode("utf-8")
        else: # normal word.
            encoding = get_key_from_value(
                encoding_json[pages[current_page]], "0x" + byte
            )
            if encoding:
                if not in_switch_sequence:
                    out += encoding

    print(f"TPSCII decoding for '0x{"".join(byte_input)}':\n{out}")


if __name__ == "__main__":
    main()

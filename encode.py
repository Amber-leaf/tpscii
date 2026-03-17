import json
import sys

def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

control_codes = {
    "0": "0x30",
    "1": "0x31",
    "2": "0x32",
    "3": "0x33",
    "4": "0x34",
    "5": "0x35",
    "6": "0x36",
    "7": "0x37",
    "8": "0x38",
    "9": "0x39",
    "nul": "0x00",
    "soh": "0x01",
    "stx": "0x02",
    "etx": "0x03",
    "eot": "0x04",
    "enq": "0x05",
    "ack": "0x06",
    "bel": "0x07",
    "bs": "0x08",
    "ht": "0x09",
    "lf": "0x0a",
    "vt": "0x0b",
    "ff": "0x0c",
    "cr": "0x0d",
    "so": "0x0e",
    "si": "0x0f",
    "dle": "0x10",
    "dc1": "0x11",
    "dc2": "0x12",
    "dc3": "0x13",
    "dc4": "0x14",
    "nak": "0x15",
    "syn": "0x16",
    "etb": "0x17",
    "can": "0x18",
    "em": "0x19",
    "sub": "0x1a",
    "esc": "0x1b",
    "fs": "0x1c",
    "gs": "0x1d",
    "rs": "0x1e",
    "us": "0x1f",
    "space": "0x20",
    "!": "0x21",
    "\"": "0x22",
    "#": "0x23",
    "$": "0x24",
    "%": "0x25",
    "&": "0x26",
    "'": "0x27",
    "(": "0x28",
    ")": "0x29",
    "*": "0x2a",
    "+": "0x2b",
    ",": "0x2c",
    "-": "0x2d",
    ".": "0x2e",
    "/": "0x2f",
    ":": "0x3a",
    ";": "0x3b",
    "<": "0x3c",
    "=": "0x3d",
    ">": "0x3e",
    "?": "0x3f",
    "@": "0x40",
    "[": "0x41",
    "]": "0x42",
    "\\": "0x43",
    "—": "0x44",
    "`": "0x45",
    "{": "0x46",
    "|": "0x47",
    "}": "0x48",
    "~": "0x49",
    "del": "0x50",
    "pnt": "0xfe",
    "pgs": "0xff"
}

def parse_tokens(text):
    output = []
    word_buffer = ""

    for letter in text:
        print(int(letter.encode("ascii").hex(),16))
        if word_buffer in control_codes:
            output.append(word_buffer)
            word_buffer = ""

        match letter:
            case "\n":
                if word_buffer:
                    output.append(word_buffer)
                word_buffer = ""
                output.append("lf")
                continue
            case " ":
                if word_buffer:
                    output.append(word_buffer)
                word_buffer = ""
                output.append("space")
                continue



        # if we are here, we must be in a word
        word_buffer += letter

    if word_buffer:
        output.append(word_buffer)

    return output

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    else:
        print(
            "Paste text to encode, then press Ctrl+D (Unix) or Ctrl+Z (Windows) when done:"
        )
        text = sys.stdin.read()

    text = text.lower().strip()

    encoding_json = json.loads(open("encoding.json").read())

    tokens = parse_tokens(text)

    print(tokens)

    last_page = 0
    out = ""

    for word in tokens:
        if not word:
            continue

        for page in encoding_json:
            page_int = int(page.removeprefix("page"))

            try:
                encoding = encoding_json[page][word]
                if encoding:
                    if page_int != last_page:
                        out += "ff"
                        out += "{:04X}".format(page_int)
                        last_page = page_int

                    out += encoding.removeprefix("0x")

            except KeyError:
                pass

    print(f"TPSCII encoding for '{text}':\n{out}")


if __name__ == "__main__":
    main()

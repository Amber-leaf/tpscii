import json
import sys

control_codes = {
    0x00: "NUL",
    0x01: "SOH",
    0x02: "STX",
    0x03: "ETX",
    0x04: "EOT",
    0x05: "ENQ",
    0x06: "ACK",
    0x07: "BEL",
    0x08: "BS",
    0x09: "HT",
    0x0A: "LF",
    0x0B: "VT",
    0x0C: "FF",
    0x0D: "CR",
    0x0E: "SO",
    0x0F: "SI",
    0x10: "DLE",
    0x11: "DC1",
    0x12: "DC2",
    0x13: "DC3",
    0x14: "DC4",
    0x15: "NAK",
    0x16: "SYN",
    0x17: "ETB",
    0x18: "CAN",
    0x19: "EM",
    0x1A: "SUB",
    0x1B: "ESC",
    0x1C: "FS",
    0x1D: "GS",
    0x1E: "RS",
    0x1F: "US",
    0x20: "SPACE",
    0x50: "DEL",
    0x21: "!",
    0x22: '"',
    0x23: "#",
    0x24: "$",
    0x25: "%",
    0x26: "&",
    0x27: "'",
    0x28: "(",
    0x29: ")",
    0x2A: "*",
    0x2B: "+",
    0x2C: ",",
    0x2D: "-",
    0x2E: ".",
    0x2F: "/",
    0x3A: ";",
    0x3B: ";",
    0x3C: "<",
    0x3D: "=",
    0x3E: ">",
    0x3F: "?",
    0x40: "@",
    0x41: "[",
    0x42: "]",
    0x43: "\\",
    0x44: "—",
    0x45: "`",
    0x46: "{",
    0x47: "|",
    0x48: "}",
    0x49: "~",
}

def parse_tokens(text):
    output = []
    word_buffer = ""

    for letter in text:
        match letter:
            case ctrl if (code := ord(ctrl)) in control_codes:
                if word_buffer:
                    output.append(word_buffer)
                output.append(control_codes[code])
                word_buffer = ""
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

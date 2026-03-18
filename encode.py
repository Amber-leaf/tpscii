import json
import sys

def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def parse_tokens(text):
    output = []
    word_buffer = ""

    for letter in text:
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

            case c if not c.isalpha():
                if word_buffer:
                    output.append(word_buffer)
                word_buffer = ""
                output.append(c)
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

        encoding = ""
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
        if not encoding:
            print(
                f"Warning: no such word '{word}'. If this is a nimisin, you might be using an outdated version of this program. We will encode '' instead."
            )

    print(f"TPSCII encoding for:\n'{text}':\n{out}")

if __name__ == "__main__":
    main()

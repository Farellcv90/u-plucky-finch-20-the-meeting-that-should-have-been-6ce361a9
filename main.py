LINE = "The meeting produced exactly one decision: to hold another meeting to decide when to decide."


def validate(text):
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(LINE))


if __name__ == "__main__":
    main()

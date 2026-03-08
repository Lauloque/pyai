def indentprint(text: str) -> None:
    print("\n".join("    " + line for line in text.split("\n")))

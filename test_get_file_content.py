from config import MAX_CHARS
from functions.get_file_content import get_file_content
from functions.indentprint import indentprint


def main() -> None:
    print("Lorem test:")
    lorem = get_file_content("calculator", "lorem.txt")
    chars = len(lorem)
    indentprint(f"Lorem is '{chars}' characters long.")
    if chars > MAX_CHARS:
        if f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]' not in lorem:
            indentprint("Failed truncation of Lorem...")
            print(lorem)
            return

    print("Result for 'main.py' file:")
    indentprint(get_file_content("calculator", "main.py"))

    print("Result for 'pkg/calculator.py' file:")
    indentprint(get_file_content("calculator", "pkg/calculator.py"))

    print("Result for '/bin/cat' file:")
    indentprint(get_file_content("calculator", "/bin/cat"))

    print("Result for 'pkg/does_not_exist.py' file:")
    indentprint(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()

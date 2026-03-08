from functions.indentprint import indentprint
from functions.write_file import write_file


def main() -> None:
    print("Result for 'lorem.txt':")
    indentprint(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print("Result for 'pkg/morelorem.txt':")
    indentprint(
        write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    )

    print("Result for '/tmp/temp.txt':")
    indentprint(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


if __name__ == "__main__":
    main()

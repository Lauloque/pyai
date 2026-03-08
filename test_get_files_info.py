from functions.get_files_info import get_files_info
from functions.indentprint import indentprint


def main() -> None:
    print("Result for current directory:")
    indentprint(get_files_info("calculator", "."))

    print("Result for 'pkg' directory:")
    indentprint(get_files_info("calculator", "pkg"))

    print("Result for '/bin' directory:")
    indentprint(get_files_info("calculator", "/bin"))

    print("Result for '../' directory:")
    indentprint(get_files_info("calculator", "../"))


if __name__ == "__main__":
    main()

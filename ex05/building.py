import sys


def scan_text(text):
    """
    text (input string): The text to scan.

    Prints the following information:
        1. The number of characters in the text
        2. The number of upper case letters
        3. The number of lower case letters
        4. The number of punctuation marks
        5. The number of spaces
        6. The number of digits
    """

    total_chars = len(text)
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation_cnt = sum(1 for char in text if char in punctuation_characters)
    space_count = sum(1 for char in text if char.isspace())
    digit_count = sum(1 for char in text if char.isdigit())

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_cnt} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """
        - Scanning the provided text and prints detailed \
            information about its character composition.

        - If no command-line argument is given, prompts the user to enter text.

        - AssertionError: If more than one argument \
            is provided via the command line.
    """

    try:
        if len(sys.argv) < 2:
            try:
                s = input("What is the text to count?\n")
                s += "\n"
            except EOFError:
                pass
        elif len(sys.argv) == 2:
            s = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        scan_text(s)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()

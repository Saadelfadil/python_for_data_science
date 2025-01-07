import sys


def iamwhat(number: int):
    return "I'm Even." if number % 2 == 0 else "I'm Odd."


def main(argv):
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        if len(argv) > 1:
            assert argv[1][0] == "-" or argv[1][0] == "+" \
                and argv[1][1:].isnumeric() \
                or argv[1].isnumeric(), "argument is not an integer"
            print(iamwhat(int(argv[1])))

    except AssertionError as msg:
        print(f'AssertionError: {msg}')
        exit(1)


if __name__ == "__main__":
    main(sys.argv)

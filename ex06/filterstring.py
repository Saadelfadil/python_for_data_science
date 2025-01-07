import sys
from ft_filter import ft_filter


def main():
    try:
        # Ensure exactly two arguments (including the script name)
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        # Get the string (S) and integer (N) from arguments
        text = sys.argv[1]
        n = int(sys.argv[2])
        # Validate input types
        if not isinstance(text, str) or not isinstance(n, int):
            raise AssertionError("the arguments are bad")
        # Use list comprehension and lambda to filter words
        result = list(ft_filter(lambda word: len(word) > n, text.split()))
        print(result)
    except ValueError as error:
        print(f"ValueError: {error}")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()

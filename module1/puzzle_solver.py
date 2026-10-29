import sys

# possible to enforce specific initial state through command line
# read from a file or use command line parameters

# display the first solution

# dict of {number: position}


def main():
    if len(sys.argv) != 2:
        print("Usage: puzzle_solver <file_name>", file=sys.stderr)
        return

    with open(sys.argv[1], 'r') as file:
        data = file.read()

    # Convert file content into integers
    numbers = [int(x) for x in data.split()]

    # Check if numbers are valid
    if sorted(numbers) != list(range(9)):
        print("Invalid numbers", file=sys.stderr)
        sys.exit(1)

    # Create dict: number -> position
    positions = {}

    for index, number in enumerate(numbers):
        positions[number] = index

    print(positions)


if __name__ == "__main__":
    main()
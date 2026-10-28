import sys

# possible to enforce specific initail state thoriyh command line
#  read from a line or use a command line parameters

# display the first solution

# def can_the_square_move():
#     if 

# # dict of {[number] : place}


# def are_numbers_valid()
#     for i in range numbers
#         if !(number >= 0 && number <=8)
#             printf("Numbers have to be in range 0 - 8", file=sys.stderr)
#             exit(1)


numbers = [int(x) for x in data.split()]

if sorted(numbers) != list(range(9)):
    print("Invalid numbers", file=sys.stderr)
    sys.exit(1)

positions = {}

for index, number in enumerate(numbers)
    positions[number] = index



def main():
    if len(sys.argv) != 2:
        print("Usage: puzzle_solver <file_name>", file=sys.stderr)
        return

    with open(sys.argv[1], 'r') as file:
        data = file.read()

    print(data)

# splitlines divides text into seperate lines
# enumerate() assigns each line an index, starting from 0

    numbers = {
        int(number): index
        for index, number in enumerate(data.splitlines())
    }
    print(numbers)


if __name__ == "__main__":
    main()
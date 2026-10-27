import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: expert_system.py <min_temp> <max_temp>")
        return

    min_temp = float(sys.argv[1])
    max_temp = float(sys.argv[2])

    print(min_temp, max_temp)


if __name__ == "__main__":
    main()
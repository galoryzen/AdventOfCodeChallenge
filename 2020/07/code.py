
def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.strip() for line in f.read().strip().split("\n")]



def main():
    groups = readFile()
    print(groups)

def part1():

def part2():


if __name__ == "__main__":
    main()

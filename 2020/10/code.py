def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(line) for line in f.read().strip().split("\n")]


def main():
    red = parseFile()
    


if __name__ == "__main__":
    main() 
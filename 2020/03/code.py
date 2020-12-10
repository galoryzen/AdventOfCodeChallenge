
def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]

def count_trees(values, dx, dy):
    x, y, c = 0,0,0
    length = len(values) - dy
    mod = len(values[0])
    while y < length:
        x = (x+dx) % mod
        y = y + dy
        if values[y][x] == "#":
            c = c + 1
    return c

def first(values):
    return count_trees(values, 3, 1)

def second(values, firstSol):
    slopes = ((1, 1), (5,1), (7,1), (1,2))
    answer = firstSol
    for slope in slopes:
        answer *= count_trees(values, slope[0], slope[1])
    return answer

def main():
    f = readFile()
    print(first(f))
    print(second(f, first(f)))

if __name__ == "__main__":
    main()
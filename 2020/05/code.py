def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line[:-1].replace("F", "0").replace("B", "1")
            .replace("L", "0").replace("R", "1") for line in f.readlines()]


def part1(seats):
    return max(seats)

def part2(seats):
    for seat in range(min(seats), int(max(seats)) + int(1)):
        if seat not in seats and (seat-1) in seats and (seat+1) in seats:
            return seat

def main():
    filee = readFile()
    #print(part1(filee))
    print(part2(filee))

if __name__ == "__main__":
    main()

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.split() for line in f.read().strip().split("\n\n")]

def part1(groups):
    i = 0
    for group in groups:
        s = ""
        for answer in group:
            s += answer
        new_str = "".join(set(s))
        i += len(new_str)
    return i
    
def part2(groups):
    result = 0
    for group in groups:
        answers = {chr(c):0 for c in range(97, 123)}

        for answer in group:
            for letter in answer:
                answers[letter] += 1

        result += sum([1 for letter in answers if answers[letter] == len(group)])
    return result

def main():
    groups = readFile()
    print(part1(groups))
    print(part2(groups))
    


if __name__ == "__main__":
    main()

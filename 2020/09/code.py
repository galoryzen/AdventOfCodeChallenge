def parseFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(line) for line in f.read().strip().split("\n")]

def part1(input, preamble):
    pointer = preamble
    while pointer != len(input):
        hey = False
        diff = pointer - preamble
        for i in range(diff, pointer):
            if input[pointer]- input[i] in input[diff:pointer]:
                hey = True
                break
        if not hey:
            return input[pointer]
        pointer +=1

def part2(input, num):
    length = len(input)
    for pointer in range(length):
        sum = input[pointer]
        nextPointer = pointer+1
        while sum < num and nextPointer < length:
            sum += input[nextPointer]
            nextPointer += 1
            if sum == num:
                helper = input[pointer:nextPointer-1]
                return max(helper) + min(helper)




def main():
    red = parseFile()
    p1 = part1(red, 25)
    p2 = part2(red, p1)
    print(p1, p2)


if __name__ == "__main__":
    main() 
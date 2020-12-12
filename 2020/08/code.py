def parseFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.strip() for line in f.read().strip().split("\n")]


"""
There is a better way to do this, probably by splitting at the start while reading file
It would save a lot of space
And it would probably be more efficient to store len(instructions) in a variable instead of calculating it everytime
"""

def run(instructions):
    visited = []
    accumulator = 0
    pointer = 0
    while pointer not in visited and pointer != len(instructions):
        helper = instructions[pointer].split()
        instruction = helper[0]
        amount = int(helper[1])
        visited.append(pointer)

        if instruction == "acc":
            accumulator += amount
            pointer += 1
        elif instruction == "jmp":
            pointer += amount
        else:
            pointer +=1
    return pointer, accumulator


def part1(instructions):
    return run(instructions)[1]

def part2(instructions):
    for i in range(len(instructions)):
        helper = instructions[i].split()
        
        if helper[0] == "jmp":

            instructions[i] = "nop "+helper[1]
            pointer, accumulator = run(instructions)
            instructions[i] = "jmp "+helper[1]

        elif helper[0] == "nop":

            instructions[i] = "jmp "+helper[1]
            pointer, accumulator = run(instructions)
            instructions[i] = "nop "+helper[1]
        
        else:
            continue

        if pointer >= len(instructions):
            return accumulator

def main():
    instructions = parseFile()
    print(part1(instructions))
    print(part2(instructions))



if __name__ == "__main__":
    main() 
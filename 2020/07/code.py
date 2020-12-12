import re
import collections
from typing import DefaultDict
from typing import Dict
from typing import List

#Reguar expressions used
LINE_RE = re.compile(r'^(\w+ \w+) bags contain (.+)$')
CHILD_RE = re.compile(r'(\d+) (\w+ \w+)')


def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.strip() for line in f.read().strip().split("\n")]

def parsePart1(input):
    parents = collections.defaultdict(list)
    for line in input:
        line_match = LINE_RE.match(line)
        assert line_match, line
        parent = line_match[1]
        rest = line_match[2]

        for _, child in CHILD_RE.findall(rest):
            parents[child].append(parent)
    return parents

def parsePart2(input):
    colors = {}
    for line in input:
        line_match = LINE_RE.match(line)
        assert line_match, line
        parent = line_match[1]
        rest = line_match[2]

        children = [(int(n), child) for n, child in CHILD_RE.findall(rest)]
        colors[parent] = children   
    return colors


def part1(input):
    seen = set()
    colors = ['shiny gold']

    while colors:
        color = colors.pop()
        seen.add(color)
        colors.extend(input[color])

    return len(seen) - 1

def part2(input):
    sum = 0
    color_tuples = [(1, 'shiny gold')]

    while color_tuples:
        amount ,color = color_tuples.pop()
        sum += amount
        color_tuples.extend(((amount * child_number), child) for child_number, child in input[color])
    
    return sum - 1


def main():
    print(part1(parsePart1(readFile())))
    print(part2(parsePart2(readFile())))


if __name__ == "__main__":
    main() 
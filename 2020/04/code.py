import re

def readFile():
    result = list()
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        for data in f.read()[:-1].split("\n\n"):
            result.append(dict(d.split(":") for d in data.replace("\n", " ").split()))
    return result

def assert_fields(data):
    return all((field in data for field in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")))

def part1(registros):
    return len(registros)

def part2(registros) -> int:
    patrones = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}",
        "cid": ".*"
    }
    return sum((all((re.fullmatch(patrones[v], registro[v]) for v in registro)) for registro in registros))

def main():
    registros = readFile()
    valid_passports = list()
    for registro in registros:
        if assert_fields(registro):
            valid_passports.append(registro)

    print(part1(valid_passports))
    print(part2(valid_passports))

if __name__ == "__main__":
    main()
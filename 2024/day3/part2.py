import re

with open("input.txt") as file:
    lines = file.read()
    lines = "do()" + lines.replace('\n', '')
    lines = lines.replace('do()', '\ndo()')
    lines = lines.replace('don\'t()', '\ndon\'t()')
    do_lines = []
    for line in lines.splitlines():
        if line.startswith("do()"):
            do_lines.append(line)
    pattern = r"mul\((\d+),(\d+)\)"

    solution = 0

    for line in do_lines:
        matches = re.findall(pattern, line)
        for match in matches:
            num1, num2 = map(int, match)
            solution += num1 * num2

    print(f"Solution: {solution}")
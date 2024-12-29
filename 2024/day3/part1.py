import re

with open("input.txt") as file:
    lines = file.readlines()

pattern = r"mul\((\d+),(\d+)\)"

solution = 0

for line in lines:
    matches = re.findall(pattern, line)
    for match in matches:
        num1, num2 = map(int, match)
        solution += num1 * num2

print(f"Solution: {solution}")


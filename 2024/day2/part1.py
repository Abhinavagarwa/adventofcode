with open("input.txt") as file:
    lines = file.readlines()

numbers_per_line=[list(map(int, line.split())) for line in lines]

safe_count = 0

for i, line in enumerate(numbers_per_line, start=1):
    valid_line = True
    direction = "neutral"
    for j in range(len(line) - 1):
        prev_direction = direction
        current_num = line[j]
        next_num = line[j + 1]
        if abs(current_num - next_num) > 3 or abs(current_num - next_num) < 1:
            valid_line = False
            break
        if current_num > next_num:
            direction = "down"
        else:  
            direction = "up"
        if direction != prev_direction and prev_direction != "neutral":
            valid_line = False
            break
    if valid_line == True:
        safe_count += 1

solution = safe_count
print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")
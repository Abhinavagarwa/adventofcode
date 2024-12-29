with open("input.txt") as file:
    lines = file.readlines()

numbers_per_line = [list(map(int, line.split())) for line in lines]

safe_count = 0

def is_line_safe(line):
    direction = "neutral"
    for j in range(len(line) - 1):
        prev_direction = direction
        current_num = line[j]
        next_num = line[j + 1]
        if abs(current_num - next_num) > 3 or abs(current_num - next_num) < 1:
            return False
        if current_num > next_num:
            direction = "down"
        else:
            direction = "up"
        if direction != prev_direction and prev_direction != "neutral":
            return False
    return True

# For loop to go line by line
for i, line in enumerate(numbers_per_line, start=1):
    if is_line_safe(line):
        safe_count += 1
    else:
        # Remove one number of the failed line at a time to see if it can become valid
        line_is_safe = False
        for k in range(len(line)):
            # Take the line from the beginning up to (but not including) K 
            # and then join it with positions k + 1 onwards, thus removing K from the list
            modified_line = line[:k] + line[k + 1:]
            if is_line_safe(modified_line):
                line_is_safe = True
                break
        if line_is_safe:
            safe_count += 1

solution = safe_count
print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")
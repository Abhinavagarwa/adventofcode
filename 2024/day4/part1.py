def count_word_occurrences(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),    
        (0, -1),   
        (1, 0),    
        (-1, 0),   
        (1, 1),    
        (1, -1),    
        (-1, 1),    
        (-1, -1),   
    ]
    
    def is_valid(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_valid(x, y, dx, dy):
                    count += 1
    return count

def main():
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()

        word = "XMAS"

        grid = [line.strip() for line in lines[0:]]

        result = count_word_occurrences(grid, word)
        print(f"Total occurrences of '{word}': {result}")

    except FileNotFoundError:
        print("Error: input.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

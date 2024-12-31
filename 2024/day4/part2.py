def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for x in range(1, rows - 1):  
        for y in range(1, cols - 1):
            if grid[x][y] == 'A':  
                
                if (
                    (grid[x - 1][y - 1] == 'M' and grid[x + 1][y + 1] == 'S' and  
                    grid[x - 1][y + 1] == 'M' and grid[x + 1][y - 1] == 'S') or 
                    (grid[x + 1][y + 1] == 'M' and grid[x - 1][y - 1] == 'S' and  
                    grid[x + 1][y - 1] == 'M' and grid[x - 1][y + 1] == 'S') or
                    (grid[x - 1][y - 1] == 'M' and grid[x + 1][y + 1] == 'S' and  
                    grid[x + 1][y - 1] == 'M' and grid[x - 1][y + 1] == 'S') or
                    (grid[x + 1][y + 1] == 'M' and grid[x - 1][y - 1] == 'S' and  
                    grid[x - 1][y + 1] == 'M' and grid[x + 1][y - 1] == 'S') 
                       
                ):
                    count += 1
    return count


def main():
        with open("input.txt", "r") as file:
            grid = [line.strip() for line in file.readlines()]

        result = count_xmas_patterns(grid)
        print(f"Total X-MAS patterns: {result}")

if __name__ == "__main__":
    main()

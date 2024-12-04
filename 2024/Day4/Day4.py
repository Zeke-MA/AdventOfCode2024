def get_input():
    f = open("input.txt", "r")
    return f.readlines()

def find_xmas(line):
    return line.count("XMAS") + line[::-1].count("XMAS")

def find_horizontal(input):
    total_xmas = 0
    for line in input:
        total_xmas += find_xmas(line)
    print(f"Total Horizontal XMAS|MASX: {total_xmas}")
    return total_xmas

def find_vertical(input):
    
    col = len(input[0]) - 1
    total_xmas = 0
    
    for i in range(col):
        column = ''.join([input[row][i] for row in range(col)])
        total_xmas += find_xmas(column)
        
    print(f"Total vertical XMAS|MASX: {total_xmas}")
    return total_xmas

def find_diagonal(input):
    rows = len(input)
    cols = len(input[0]) - 1
    total_xmas = 0
    
    for d in range(-rows + 1, cols):
        left_right = "".join([input[i][i - d] for i in range(max(0, d), min(rows, cols + d))])
        total_xmas += find_xmas(left_right)
        
    for d in range(rows + cols - 1): 
        right_left = "".join([input[i][d - i] for i in range(max(0, d - cols + 1), min(rows, d + 1))])
        total_xmas += find_xmas(right_left)
        
    print(f"Total diagonal XMAS|MASX: {total_xmas}")
    return total_xmas

def xmas_x(input):
    col = len(input[0])
    row = len(input)
    total_xmas = 0
    
    
    for i in range(1, row - 1):
        for c in range(1, col - 1):
            if input[i][c] == "A":
                top_left = input[i - 1][c - 1]
                top_right = input[i - 1][c + 1]
                bottom_left = input[i + 1][c - 1]
                bottom_right = input[i + 1][c + 1]
                
                if top_left == "M" and bottom_right == "S":
                    if (top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M"):
                        total_xmas += 1
                elif top_right == "M" and bottom_left == "S":
                    if (top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M"):
                        total_xmas += 1
                elif top_left == "S" and bottom_right == "M":
                    if (top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M"):
                        total_xmas += 1
                elif top_right == "S" and bottom_left == "M":
                    if (top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M"):
                        total_xmas += 1
    print(f"Total diagonal XMAS|MASX: {total_xmas}")
    return total_xmas

def main():
    input = get_input()
    total_p1 = find_horizontal(input) + find_vertical(input) +  find_diagonal(input)
    print(f"Total part 1 matches: {total_p1}")
    xmas_x(input)

    
main()


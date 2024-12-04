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
                   

def main():
    input = get_input()
    result = find_horizontal(input) + find_vertical(input) +  find_diagonal(input)
    print(result)
    
   
    
main()
MOVEMENT = ["^", ">", "v", "<"] 

def file_read():
    with open("input.txt", "r") as f:
        return [row.strip("\n") for row in f.readlines()]
    
def find_starting_point(rows):
    for i in range(len(rows)):
        if "^" in rows[i]:
            row_idx = i
            col_idx = rows[i].index("^")
            break
    return row_idx, col_idx

def main():
    input = file_read()
    print(input)
    print(find_starting_point(input))

main()
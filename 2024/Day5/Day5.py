import statistics

def file_read():
    with open("input.txt", "r") as f:
        return [x.strip("\n") for x in f.readlines()]
    
def read_instructions():
    with open("input_commas.txt", "r") as f:
        return  [[int(num) for num in x.strip("\n").split(",")] for x in f.readlines()]
    
def rules(input):
    rules = {}
    for i in input:
        split_pages = i.split("|")
        if int(split_pages[0]) not in rules:
            rules[int(split_pages[0])] = [int(split_pages[1])]
        else:
            rules[int(split_pages[0])].append(int(split_pages[1]))
    return rules
    
def part1(rules, instructions):
    sum_of_middle = 0
    
    for i in instructions:
        manual_valid = True
        
        for k in range(len(i) - 1):
            if i[k] in rules:
                if i[k + 1] not in rules[i[k]]:
                    manual_valid = False
                    break
                
        if manual_valid:
            print(statistics.median(i))
            sum_of_middle += statistics.median(i)
            
    print(f"The sum of the valid middle pages part1: {sum_of_middle}")
    return sum_of_middle
    
def main():
    input = file_read()
    instructions = read_instructions()
    rule = rules(input)
    part1(rule,instructions)
    
main()
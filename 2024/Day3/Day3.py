import re

def get_input():
    f = open("input.txt", "r")
    return f.read()

def mull_it_over(input):
    sum_of_product = 0
    
    matches = re.findall(r"mul\(\d+,\d+\)", input)
    
    for mul in matches:
        first_digit = re.search(r"\d+", mul)
        second_digit = re.search(r"(?<=,)\d+(?=\))", mul)
        sum_of_product += int(first_digit.group(0)) * int(second_digit.group(0))
        
    print(f"The sum of products part 1: {sum_of_product}")
    
    return sum_of_product

def do_or_dont(input):
    sum_of_product = 0
    
    pattern = r"\bdon't\(\)|\bdo\(\)|mul\(\d+,\d+\)"
    
    matches = re.findall(pattern, input)
    
    do = True
    
    for mul in matches:
        if mul == "do()":
            do = True
            continue
            
        if mul == "don't()":
            do = False
            continue
        
        if do:
            first_digit = re.search(r"\d+", mul)
            second_digit = re.search(r"(?<=,)\d+(?=\))", mul)
            sum_of_product += int(first_digit.group(0)) * int(second_digit.group(0))
        
    print(f"The sum of products part 2: {sum_of_product}")
    
    return sum_of_product

def main():
    
    input = get_input()
    mull_it_over(input)
    do_or_dont(input)
    
    
main()
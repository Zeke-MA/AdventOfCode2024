def file_read():
    with open("input.txt", "r") as f:
        return [[int(x) for x in line.split()] for line in f]
    
def safe_check_p1(input):
    total_safe = 0
    
    for report in input:
        if is_safe(report):
            total_safe += 1
    print(f"Total safe levels part 1: {total_safe}")        
    return total_safe


def safe_check_p2(input):
    total_safe = 0
    for report in input:
        for i in range(len(report)):
            
            combined = report[:i] + report[i+1:]
            
            if is_safe(combined):
                total_safe += 1
                break
    print(f"Total safe levels part 2: {total_safe}")
    return total_safe

def is_safe(report):
    order = False
    
    if report == sorted(report, reverse=False):
        order = True
    elif report == sorted(report, reverse=True):
        order = True
    
    
    tolerance = True
    
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if not 1 <= diff <= 3:
            tolerance = False
            
    return order and tolerance
        
def main():
    input = file_read()
    safe_check_p1(input)
    safe_check_p2(input)

main()



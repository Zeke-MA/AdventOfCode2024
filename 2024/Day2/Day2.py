def file_read():
    f = open("input.txt", "r")
    f = f.readlines()
    input =  [[int(x) for x in line.split()] for line in f]
    return input

def safe_check(input):
    total_safe = 0
    for i in input:
        if is_safe_decrease(i) or is_safe_increase(i):
            total_safe += 1
    return total_safe
                
        
def is_safe_decrease(report):
    safe = True
    fault = 0
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff > 0 and diff <= 3 and fault < 1:
            if report[i] > report[i + 1]:
                safe = True
            else:
                safe = True
                fault += 1
        elif diff > 0 and diff <= 3 and fault >= 1:
            if report[i] > report[i + 1]:
                safe = True
            else:
                return False
        else:
            return False
    return safe
    
    
def is_safe_increase(report):
    safe = True
    fault = 0
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff > 0 and diff <= 3 and fault < 1:
            if report[i] < report[i + 1]:
                safe = True
            else:
                safe = True
                fault += 1
        elif diff > 0 and diff <= 3 and fault >= 1:
            if report[i] < report[i + 1]:
                safe = True
            else:
                return False
        else:
            return False
      
    return safe
    
# Correct Ans is 601 account for corner cases
print(safe_check(file_read()))
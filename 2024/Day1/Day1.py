from collections import Counter
import datetime

def file_read():
    f = open("input.txt", "r")
    f = f.readlines()
    input = [x.strip().split() for x in f]
    return input
    
def get_difference(input):
    total_diff = 0
    sim_score = 0
    left = []
    right = []
    
    for i in input:
        left.append(int(i[0]))
        right.append(int(i[1]))
        
    left_sort = sorted(left)
    right_sort = sorted(right)
    
    counts = Counter(right_sort)
    
    for i in range(len(left_sort)):
        total_diff += abs(left_sort[i] - right_sort[i])
        
    for i in range(len(left_sort)):
        sim_score += counts[left_sort[i]] * left_sort[i]
    return total_diff, sim_score

            
start_time = datetime.datetime.now()
input = file_read()
print(get_difference(input))
end_time = datetime.datetime.now()
duration = end_time - start_time
print(f"Ran for: {duration}")
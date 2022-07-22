# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
from collections import Counter

def get_probabilty(list_idx)->float:
    if len(list_idx)==0: return 0

    occurence = 0
    all_possible_combination = 0
    for comb in combinations(range(n), k):
        for idx in comb:
            if idx in list_idx:
                occurence += 1
                break
            
        all_possible_combination +=1
    
    return occurence/all_possible_combination
    
if __name__ == "__main__":
    n = int(input())
    list_idx= set()
    for idx, char in enumerate(input().split()):
        if char == 'a': list_idx.add(idx)
    k = int(input())
    print(get_probabilty(list_idx))
    
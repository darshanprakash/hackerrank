from itertools import combinations

def monsoon_umbrellas(target, numbers):
    results = []
    for x in range(len(numbers)):
        results.extend(
            [   
                combo for combo in combinations(numbers ,x)  
                    if sum(combo) == target
            ]   
        )
    min_len_list=[]
    for i in results:
        min_len_list.append(len(i))
        
    print min(min_len_list)

if __name__ == "__main__":
    monsoon_umbrellas(14,[1,3,7,9,11,2,4])
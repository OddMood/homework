def top_frequent(arr: list, k: int) -> list:
    dict_of_counts = {}
    max_frequency = 0
    for i in arr:
        dict_of_counts[i] = dict_of_counts.get(i,0)+1
        if dict_of_counts[i]>max_frequency:
            max_frequency = dict_of_counts[i]
    list_of_frequency = [[]] * max_frequency
    for key, value in dict_of_counts.items():
        list_of_frequency[value].append(key)
    

if __name__ == '__main__':
    arr = [int(i) for i in input()[1:-1].split(',')]
    k = int(input())
    print(top_frequent(arr, k))
    

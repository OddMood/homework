def top_frequent(_arr: list, _k: int) -> list:
    dict_of_counts = {}
    max_frequency = 0

    for i in arr:
        dict_of_counts[i] = dict_of_counts.get(i, 0) + 1
        if dict_of_counts[i] > max_frequency:
            max_frequency = dict_of_counts[i]

    list_of_frequency = [[] for _ in range(max_frequency + 1)]
    for key, value in dict_of_counts.items():
        list_of_frequency[value].append(key)

    answer = []
    for i in reversed(list_of_frequency):
        answer.extend(i)
        _k -= len(i)
        if _k <= 0:
            break
    return answer


if __name__ == '__main__':
    arr = [int(i) for i in input()[1:-1].split(',')]
    k = int(input())
    print(top_frequent(arr, k))

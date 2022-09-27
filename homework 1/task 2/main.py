def count_triplets(arr: list, a: int, b: int, c: int) -> int:
    from itertools import combinations

    counter = 0
    for i, j, k in combinations(arr,3):
        if abs(i-j) <= a and abs(j-k) <= b and abs(i-k) <= c:
            counter += 1
    return counter


if __name__ == '__main__':
    arr = [int(i) for i in input()[1:-1].split(',')]
    a = int(input())
    b = int(input())
    c = int(input())
    print(count_triplets(arr, a, b, c))

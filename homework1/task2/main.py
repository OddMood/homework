def count_triplets(_arr: list, _a: int, _b: int, _c: int) -> int:
    from itertools import combinations

    counter = 0
    for i, j, k in combinations(_arr, 3):
        if abs(i - j) <= _a and abs(j - k) <= _b and abs(i - k) <= _c:
            counter += 1
    return counter


if __name__ == '__main__':
    arr = [int(i) for i in input()[1:-1].split(',')]
    a = int(input())
    b = int(input())
    c = int(input())
    print(count_triplets(arr, a, b, c))

class MedianFinder:
    def __init__(self):
        self.list = []

    def add_num(self, number: int) -> None:
        index = 0
        for index, elem in enumerate(self.list):
            if elem >= number:
                break
        else:
            index += 1
        self.list.insert(index, number)
        return

    def find_median(self) -> float:
        length = len(self.list)
        if length == 0:
            return .0
        if length % 2 == 0:
            return (self.list[length // 2 - 1] + self.list[length // 2]) / 2
        else:
            return float(self.list[length // 2])

    def __repr__(self):
        return f"list: {self.list}"


if __name__ == "__main__":
    a = MedianFinder()
    a.add_num(1)
    print(a)
    print(a.find_median())
    a.add_num(2)
    print(a)
    print(a.find_median())
    a.add_num(10)
    print(a)
    print(a.find_median())
    a.add_num(2)
    print(a)
    print(a.find_median())
    a.add_num(2)
    print(a)
    print(a.find_median())
    a.add_num(4)
    print(a)
    print(a.find_median())
    a.add_num(3)
    print(a)
    print(a.find_median())
    a.add_num(4)
    print(a)
    print(a.find_median())

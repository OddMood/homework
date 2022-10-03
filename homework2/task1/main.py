class MedianFinder:
    def __init__(self):
        self.list = []
        self.middle_index = [-1, 0]

    def add_num(self, number: int):
        index = 0
        for index, elem in enumerate(self.list):
            if elem >= number:
                break
        else:
            index += 1
        self.list.insert(index, number)
        if self.middle_index[0] == self.middle_index[1]:
            self.middle_index[1] += 1
        else:
            self.middle_index[0] += 1
        return

    def find_median(self) -> float:
        if len(self.list) == 0:
            return .0
        return (self.list[self.middle_index[0]] + self.list[self.middle_index[1]]) / 2

    def __repr__(self):
        return f"list: {self.list}, middle_index: {(self.middle_index[0] + self.middle_index[1]) / 2}"


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

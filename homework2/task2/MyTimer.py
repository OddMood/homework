import time


class MyTimer:
    def __init__(self, units):
        if units in ("s", "m", "h"):
            self.units = units
        else:
            raise ValueError("Wrong name of units")

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.spent_time = self.end_time - self.start_time

    def elapsed_time(self):
        if self.units == "s":
            return self.spent_time
        if self.units == "m":
            return self.spent_time/60
        if self.units == "h":
            return self.spent_time/3600
        raise ValueError("Wrong name of units")


if __name__ == "__main__":
    print("qq")
    with MyTimer(units="s") as t:
        time.sleep(10)
    print(t.elapsed_time())

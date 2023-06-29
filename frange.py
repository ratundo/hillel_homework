#Створити frange ітератор. Який буде працювати з float.

class Frange:
    def __init__(self, start, limit, step):
        self.start = start
        self.limit = limit
        self.step = step

    def __next__(self):
        if self.step > 0 and self.start >= self.limit:
            raise StopIteration('Limit is exceeded')
        elif self.step < 0 and self.start <= self.limit:
            raise StopIteration('Limit is exceeded')
        result = self.start
        self.start += self.step
        return result

    def __iter__(self):
        return self


for i in Frange(1, -25, -0.5):
    print(i)
class CallIns:
    def __init__(self):
        self.sum = 0

    def __call__(self, *args):
        for i in args:
            self.sum += i
        return f'summary is: {self.sum}'


summary1 = CallIns()
print(summary1(5, 7, 8))

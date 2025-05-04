class Buffer:
    def __init__(self):
        self.data = []

    def add(self, values):
        self.data.extend(values)
        while len(self.data) >= 5:
            group = self.data[:5]
            print(sum(group))
            self.data = self.data[5:]

    def get_current_part(self):
        return self.data
        

buf = Buffer()
buf.add([1, 2, 3])
buf.add([4, 5, 6])
buf.add([7, 8, 9, 10, 11])

class Unique(object):
    def __init__(self, data, **kwargs):
        self.used_elements = set() 
        self.data = list(data)
        self.index = 0

        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False
        
    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                if self.ignore_case:
                    current = self.data[self.index].lower() 
                else:
                    current = self.data[self.index]     
                self.index = self.index + 1
                if current not in self.used_elements:
                    self.used_elements.add(current)
                    return current

def main():
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = ['a', 'A', 'b', 'b', 'a', 'B', 'A', 'a']

    unique_gen1 = Unique(data1)
    for i in unique_gen1:
        print(i, end = " ")

    print(" ")
    unique_gen2 = Unique(data2)
    for i in unique_gen2:
        print(i, end = " ")

    print(" ")
    unique_gen3 = Unique(data2, ignore_case=True)
    for i in unique_gen3:
        print(i, end = " ")

if __name__ == "__main__":
    main()
class ArrayList:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def append(self, element: str):
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Only single characters allowed")
        self.data.append(element)

    def insert(self, element: str, index: int):
        if index < 0 or index > len(self.data):
            raise IndexError("Invalid index")
        self.data.insert(index, element)

    def delete(self, index: int):
        if index < 0 or index >= len(self.data):
            raise IndexError("Invalid index")
        return self.data.pop(index)

    def deleteAll(self, element: str):
        self.data = [e for e in self.data if e != element]

    def get(self, index: int):
        if index < 0 or index >= len(self.data):
            raise IndexError("Invalid index")
        return self.data[index]

    def clone(self):
        new_list = ArrayList()
        new_list.data = self.data.copy()
        return new_list

    def reverse(self):
        self.data.reverse()

    def findFirst(self, element: str):
        for i, e in enumerate(self.data):
            if e == element:
                return i
        return -1

    def findLast(self, element: str):
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] == element:
                return i
        return -1

    def clear(self):
        self.data.clear()

    def extend(self, other):
        if not isinstance(other, ArrayList):
            raise ValueError("Must be an instance of ArrayList")
        self.data += other.data.copy()

    def __str__(self):
        return ''.join(self.data)

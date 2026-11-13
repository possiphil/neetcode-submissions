class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def getIndex(self, key: int) -> int:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        i = self.getIndex(key)
        if i == -1:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[i] = value


    def get(self, key: int) -> int:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.values[i]
        return -1

    def remove(self, key: int) -> None:
        i = self.getIndex(key)
        if i != -1:
            del self.keys[i]
            del self.values[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
class Test:
    __list = []

    def __init__(self):
        print("construction")

    def __del__(self):
        print("destruct")

    def __str__(self):
        return "a string version of Test"

    def __getitem__(self, key):
        return self.__list[key]

    def len(self):
        return len(self.__list)

    def Add(self, value):
        self.__list.append(value)

    def Remove(self, index):
        del self.__list[index]

    def DisplayItems(self):
        for i in self.__list:
            print(i)
    
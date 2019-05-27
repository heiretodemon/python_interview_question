class Car:
    def __init__(self, name, loss):
    # loss [价格， 油耗， 公里数]
        self.name = name
        self.loss = loss

    def getName(self):
        return self.name

    def getPrice(self):
        return self.loss[0]

    def getLoss(self):
        return self.loss[1] * self.loss[2]

BMW = Car('宝马', [60, 8, 500])  # 实例化一个宝马对象
print(getattr(BMW, 'name')) 
print(dir(BMW)) # 获取所有属性和方法
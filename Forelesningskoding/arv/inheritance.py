class Animal:  # parent / forelder element
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


class HoneyBadger(Animal):  # child / barne-element
    def __init__(self, name, age, sgiven=0):
        super().__init__(name, age) # IKKE self
        self.sgiven = sgiven


dyr1 = HoneyBadger("Emil Berglund", 3, 0)
print(dyr1.get_name())
print(dyr1.sgiven)
# 
class AClass():
    name = "Pasha"

    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name

    def __repr__(self):
        return "<clas AClass()>"

    def __str__(self):
        return f"{self.name}"

    def __setattr__(self, name, value):
        print(name, value, "Установка зачения")
        super().__setattr__(name, value)

if __name__ == '__main__':
    a = AClass("A", 'object')
    b = AClass("B", 'object')
    a.attr1 = 1
    print(dir(a))
    print(dir(b))
    print(a.__dict__)
    print(b.__dict__)
    print(a.name)
    print(b.name)
    print(a.first_name)
    print(b.first_name)
    print(a)
    print(b)

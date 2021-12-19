


class Person():
    def __init__(self, sex, name):
        self.sex = sex
        self.name = name
    
    def tostring(self):
        return self.sex + ":" + self.name + "\n"
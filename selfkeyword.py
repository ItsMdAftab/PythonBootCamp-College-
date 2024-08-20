class student:
    def __init__(self,name,rno,age):
        self.name=name
        self.rno=rno
        self.age=age
    def display(self):
        print("name:{}".format(self.name))
        print("rno:{}".format(self.rno))
        print("age:{}".format(self.age))
s1=student("ajay",12,23)
s2=student("k1",25,34)
s1.display()
s2.display()

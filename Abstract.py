#abstraction
from abc import ABC#importing abstract base calss form ABC(Abstrct base class):
class polygon :
    def sides ():
        pass
class triangle (polygon):
    def sides(self):
        print("three sides ")
class square (polygon):
    def sides(self):
        print("four sides ")
    def sides(self):
        print("four sides ")
t=triangle()
t.sides()
s=square()
s.sides()
